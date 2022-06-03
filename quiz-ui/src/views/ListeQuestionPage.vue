<template>
  <h1>Question list page</h1>
  <div v-for="question in this.questionList" v-bind:key="question.position">
    <router-link to="'question/'+question.position" >{{ question.position }} - {{ question.title }} </router-link>
  </div>
</template>

<script>
import AdminApiService from "@/services/AdminApiService";

export default {
  name: "AdminPage",
  data() {
    return {
      questionList: [],
    };
  },
  async created() {
    console.log("Composant Admin page 'created'");
    let response = await AdminApiService.getAllQuestion();
    this.questionList = response.data
    console.log(this.questionList);
  },

  methods: {},
};
</script>

<style>
</style> 