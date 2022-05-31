<template>
  <p>{{ question.title }}</p>
  <p>{{ question.text }}</p>
  <img v-if="question.image" :src="question.image" />
  <a @click="$emit('answer-selected', 0)">La réponse A</a>
  <a @click="$emit('answer-selected', 1)">La réponse B</a>
  <a @click="$emit('answer-selected', 2)">La réponse C</a>
  <a @click="$emit('answer-selected', 3)">La réponse D</a>
</template>

<script>
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],
  data() {},
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