<template>
  GG {{currentPlayer}}, tu as fini avec un score de {{finalScore}}
  Tu es {{scoreClassement}} sur {{numberOfParticipant}}
  <router-link to="/">Retour a l'acceuil</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsManager",
  components: {
  },

  data() {
    return {
      currentPlayer :"",
      numberOfParticipant:0,
      finalScore:0,
      scoreBoard:[],
      scoreClassement:0
    };
  },

  async created() {
    console.log("Composant VotreScore 'created'");
    this.currentPlayer = participationStorageService.getPlayerName();
    this.finalScore = parseInt(participationStorageService.getParticipationScore());

    let tempQuizzInfo = await  quizApiService.getQuizInfo();

    let tempBoard = [];
    tempQuizzInfo.data.scores.forEach(function(participant){
      tempBoard.push(participant.score);
    })

    tempBoard.push(this.finalScore);

    this.scoreBoard = tempBoard;
    this.numberOfParticipant = this.scoreBoard.length;
    
    this.scoreBoard.sort(function(a, b) {return a - b;});

    console.log(this.scoreBoard);
    this.scoreBoard.forEach((el, index) => {
      if (el < this.finalScore){
        this.scoreClassement =  this.numberOfParticipant - index ;
        return;
      } 
    })

  },
  unmounted(){
    participationStorageService.clear()
  },
};
</script>

<style>
</style> 