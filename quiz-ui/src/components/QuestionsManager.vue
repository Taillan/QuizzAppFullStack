<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QDisplay
    :question="currentQuestion"
    @answer-selected="answerClickedHandler"
  />
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsManager",
  components: {
    QDisplay: QuestionDisplay,
  },

  data() {
    return {
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 50000,
      currentQuestion: {},
      currentAnswer: [],
    };
  },

  created() {
    console.log("Composant QuestionsManager 'created'");
  },

  async beforeCreate() {
    let tempQuestion = await quizApiService.getQuestionByPosition(1);
    let tempQuizzInfo = await quizApiService.getQuizInfo();

    console.log("number of question :", tempQuizzInfo.data.size);
    this.totalNumberOfQuestion = tempQuizzInfo.data.size;
    this.currentQuestion = tempQuestion.data;
  },

  methods: {
    async loadQuestionByPosition() {
      let tempQuestion = await quizApiService.getQuestionByPosition(
        this.currentQuestionPosition
      );

      this.currentQuestion = tempQuestion.data;
    },

    async endQuiz() {
      let payload = {
        playerName: participationStorageService.getPlayerName(),
        answers: this.currentAnswer,
      };
      console.log("payload : ", payload);
      await quizApiService.postNewParticipation(payload);
      this.$router.push("/");
    },

    answerClickedHandler(Answer) {
      this.currentAnswer.push(Answer);
      if (this.currentQuestionPosition < this.totalNumberOfQuestion) {
        this.currentQuestionPosition = this.currentQuestionPosition + 1;
        this.loadQuestionByPosition();
      } else {
        this.endQuiz();
      }
    },
  },
};
</script>

<style>
</style> 