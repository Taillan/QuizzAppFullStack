<template>
  <h1>Question Edition page</h1>
    <QForm 
      actionForm="Edit Question"
    @form-completed="editQuestion"/>
</template>

<script>

export default {
  name: "QuestionEdition",
  props: {
    position: Number,
  },
  data() {
    return {
    };
  },

  methods: {}
};
</script>

<style>
</style> 