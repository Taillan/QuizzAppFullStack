<template>
  <div class="LoginPage">
    <input type="Password" placeholder="Password" v-model="password" />
    <button class="btn btn-primary" @click="login ">Login</button>
    <h1 v-if="wrongpassword" style="color:red">Wrong password</h1>
  </div>
</template>

<script>
import AdminStorageService from "@/services/AdminStorageService";
import AdminApiService from "@/services/AdminApiService";


export default {
  name: "LoginPage",
  data() {
    return {
      wrongpassword:false,
      password: "",
    };
  },
  methods: {
    async created() {
      console.log("Composant LoginPage page 'created'");
    },
    async login(){
      let response 
      try{
      response = await AdminApiService.postLogin(this.password);
      AdminStorageService.saveAdminToken(response.data.token);
      this.$router.push("/admin");
      }catch(error){
        this.wrongpassword=true;
      }

    }
  },
};
</script>

<style>
@media (min-width: 1024px) {
}
</style>