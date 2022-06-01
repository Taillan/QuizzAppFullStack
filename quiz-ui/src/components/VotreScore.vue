<template>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import VotreScore from "@/components/VotreScore.vue";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionsManager",
  components: {
    QDisplay: QuestionDisplay,
    VScore: VotreScore,
  },

  data() {
    return {
    };
  },

  created() {
    console.log("Composant VotreScore 'created'");
  },

  methods: {
  },
};
</script>

<style>
</style> 