<template>
  <p>{{ question.title }}</p>
  <p>{{ question.text }}</p>
  <img v-if="question.image" :src="question.image" />
  <div
    v-for="answerEntry in this.question.possibleAnswers"
    v-bind:key="answerEntry.text"
  >
    <button class="btn btn-primary" @click="$emit('answer-selected', answerEntry.isCorrect)" value="">
      {{ answerEntry.text }}
    </button>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],

  async created() {
    console.log("Composant QuestionsDisplay 'created'");
  },
  methods: {},
  props: {
    question: {
      type: Object,
    },
  },
};
</script>

<style>
</style> 