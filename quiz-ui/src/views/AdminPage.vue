<template>
  <div class="AdminPage">
    <div class="LoginDiv" v-if="!this.token">
      <input type="Password" placeholder="Password" v-model="password" />
      <button class="btn btn-primary" @click="login">Login</button>
      <h1 v-if="wrongpassword" style="color:red">Wrong password</h1>
    </div>

    <div class="AdminModeDiv" v-if="this.token">
      
      <h1>AdminMode :</h1>
      <button class="btn btn-primary" @click="deconnexion">Deconnexion</button>
      <br>
      <QList v-if="this.adminMode=='QuestionsList'" @question-selected="questionSelected"/>
      <QEdit v-if="this.adminMode=='QuestionsEdition'" @goBack="this.adminMode='QuestionsList';" :position="questionSelectedPosition"/>
      <QDisplay v-if="this.adminMode=='QuestionAdminDisplay'" @goBack="this.adminMode='QuestionsList';" @goEdit="this.adminMode='QuestionsEdition';" :questionPosition="questionSelectedPosition"/>
    </div>
  </div>
</template>

<script>
import AdminStorageService from "@/services/AdminStorageService";
import AdminApiService from "@/services/AdminApiService";
import QuestionsEdition from "@/components/Admin/QuestionsEdition.vue";
import QuestionAdminDisplay from "@/components/Admin/QuestionAdminDisplay.vue";
import QuestionsList from "@/components/Admin/QuestionsList.vue";

export default {
  name: "AdminPage",
  components: {
    QList: QuestionsList,
    QEdit: QuestionsEdition,
    QDisplay: QuestionAdminDisplay,
  },
  data() {
    return {
      wrongpassword:false,
      password: "",
      token:"",
      adminMode:"QuestionsList",
      questionSelectedPosition:null,
    };
  },
  methods: {
    async created() {
      console.log("Composant AdminPage page 'created'");
    },
    questionSelected(position){
      this.questionSelectedPosition = position;
      this.adminMode='QuestionAdminDisplay';
    }
    ,
    async login(){
      let response 
      try{
      response = await AdminApiService.postLogin(this.password);
      this.token=response.data.token;
      AdminStorageService.saveAdminToken(this.token);
      }catch(error){
        this.wrongpassword=true;
      }

    },
    deconnexion(){
      console.log("Deconnexion");
      AdminStorageService.clear();
      this.token="";
    },
  },
};
</script>

<style>
</style>
