<template>
  <div class="NewQuizzPage">
    <p>Admin:</p>
    <router-link to="/question-list">Liste des questions</router-link>
  </div>
</template>

<script>

export default {
  name: "NewQuizzPage",
  data() {
    return {
    };
  },
  methods: {
    async created() {
      console.log("Composant AdminPage page 'created'");
    },
  },
};
</script>

<style>
@media (min-width: 1024px) {
}
</style>
