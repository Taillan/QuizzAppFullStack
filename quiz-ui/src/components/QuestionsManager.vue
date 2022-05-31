<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay
    :question="currentQuestion"
    @click-on-answer="answerClickedHandler"
  />
</template>

<script>
export default {
  name: "QuestionsManager",
  components: {
    QuestionDisplay,
  },
  data() {},
  methods: {
    async created() {
      
    },
    async loadQuestionByPosition(position){

    },
    async endQuiz(){
      
    }
  },
  props: {
    emits: ["answer-selected"],
    question: {
      type: Object,
    },
  },
};
</script>

<style>
</style> 