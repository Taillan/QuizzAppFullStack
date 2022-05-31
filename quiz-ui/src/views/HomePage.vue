<template>
  <h1>Home page</h1>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    var quizInfoApiResult = {
      data: {
        scores: [
          { date: "01-01-2021", score: 20, playerName: "Mathieu" },
          { date: "01-02-2021", score: 25, playerName: "Vincent" },
        ],
      },
    }; //await quizApiService.getQuizInfo();
    this.registeredScores = quizInfoApiResult.data.scores;
    console.debug("Score :", this.registeredScores);
  },
};
</script>

<style>
</style> 