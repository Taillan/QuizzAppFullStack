<template>
  <div class="NewQuizzPage">
    <p>Saisissez votre nom:</p>
    <input type="Username" placeholder="username" v-model="username" />
    <button class="btn btn-primary" @click="launchNewQuiz">GO !</button>
    <p>{{ username }}</p>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizzPage",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    async created() {
      console.log("Composant NewQuizzPage page 'created'");
    },
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      console.log("Launch new quiz with", this.username);
      this.$router.push("/questions");
    },
  },
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
