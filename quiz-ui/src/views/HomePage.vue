<template>
  <h1>Home page</h1>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
  <div v-for="scoreEntry in this.registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    let tempQuizScores = await quizApiService.getQuizInfo();
    this.registeredScores = tempQuizScores.data.scores;
    console.debug("Score :", this.registeredScores);
  },

  methods: {},
};
</script>

<style>
</style> 