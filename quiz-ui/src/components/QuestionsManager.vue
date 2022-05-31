<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  Current score is : {{ currentScore }}
  <QDisplay
    :question="currentQuestion"
    @click-on-answer="answerClickedHandler"
  />-
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from "@/components/QuestionDisplay.vue";

export default {
  name: "QuestionsManager",
  components: {
    QDisplay: QuestionDisplay,
  },

  props: {
    emits: ["answer-selected"],
  },

  data() {
    return {
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 5,
      currentQuestion: {},
      currentScore: 0,
    };
  },

  created() {
    console.log("Composant QuestionsManager 'created'");
  },

  async beforeCreate() {
    let tempQuestion = await quizApiService.getQuestionByPosition(1);

    this.currentQuestion = tempQuestion.data;
  },

  methods: {
    async loadQuestionByPosition() {
      console.log("load Question in Position " + this.currentQuestionPosition);
      let tempQuestion = await quizApiService.getQuestionByPosition(
        this.currentQuestionPosition
      );

      this.currentQuestion = tempQuestion.data;
      console.log("new question content : ", this.currentQuestion);
    },

    async endQuiz() {
      this.currentQuestionPosition = 1;
      this.$router.push("/");
    },

    answerClickedHandler() {
      this.currentQuestionPosition = this.currentQuestionPosition + 1;
      if ($event) {
        currentScore++;
      }
      if (this.currentQuestionPosition < this.totalNumberOfQuestion) {
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