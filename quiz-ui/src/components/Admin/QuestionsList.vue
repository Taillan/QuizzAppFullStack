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
    <router-link to="" @click="$emit('question-selected', question.position)" >{{ question.position }} - {{ question.title }} </router-link>
  </div>
</template>

<script>
import AdminApiService from "@/services/AdminApiService";
import AdminStorageService from "@/services/AdminStorageService";
import QuestionForm from "@/components/Admin/QuestionForm.vue";

export default {
  name: "QuestionList",
  emits: ["question-selected"],
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
    this.updateQuestionList();
  },

  methods: {
    async addNewQuestion(text,title,image,position,textA,answerA,textB,answerB,textC,answerC,textD,answerD){
      await AdminApiService.postAddQuestion(text,title,image,parseInt(position),textA,answerA,textB,answerB,textC,answerC,textD,answerD,AdminStorageService.getAdminToken());
      this.showForm = false;
      this.updateQuestionList();
    },
    async updateQuestionList(){
      let response = await AdminApiService.getAllQuestion();
      this.questionList = response.data.sort(function(a, b) {return  a.position -b.position;});
    }
  },
};
</script>

<style>
</style> 