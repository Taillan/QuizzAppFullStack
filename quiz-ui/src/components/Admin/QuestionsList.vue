<template>
  <h1>Question list page</h1>
    <button class="btn btn-primary" @click="this.showForm = !this.showForm">Add New Question</button>
    <br>
    <div class="AddQuestionDiv" v-if="this.showForm">
      <QForm 
      actionForm="Send Question"
    @form-completed="addNewQuestion"/>
    </div>
  <div v-for="question in this.questionList" v-bind:key="question.position">
    <router-link :to="'question'+question.position" >{{ question.position }} - {{ question.title }} </router-link>
  </div>
</template>

<script>
import AdminApiService from "@/services/AdminApiService";
import AdminStorageService from "@/services/AdminStorageService";
import QuestionForm from "@/components/Admin/QuestionForm.vue";

export default {
  name: "QuestionList",
  components: {
    QForm: QuestionForm,
  },
  data() {
    return {
      showForm:false,
      questionList: [],
    };
  },
  async created() {
    console.log("Composant Admin page 'created'");
    let response = await AdminApiService.getAllQuestion();
    this.questionList = response.data
    console.log(this.questionList);
  },

  methods: {
    async addNewQuestion(text,title,image,position,textA,answerA,textB,answerB,textC,answerC,textD,answerD){
      await AdminApiService.postAddQuestion(text,title,image,parseInt(position),textA,answerA,textB,answerB,textC,answerC,textD,answerD,AdminStorageService.getAdminToken());
    this.showForm = false;
  },},
};
</script>

<style>
</style> 