<template>
  <div class="QuestionForm">
    <input type="Username" placeholder="title" v-model="username" />
    <br>
    <textarea v-model="message" placeholder="text"></textarea>
    <br>
    <textarea v-model="message" placeholder="position"></textarea>
    <br>
    <textarea v-model="message" placeholder="Answer A"></textarea>
    <input type="radio" id="one" value="A" v-model="picked">
    <label for="AnswerA">IsCorrect</label>
    <br> 
    <textarea v-model="message" placeholder="Answer B"></textarea>
    <input type="radio" id="one" value="B" v-model="picked">
    <label for="AnswerB">IsCorrect</label>
    <br> 
    <textarea v-model="message" placeholder="Answer C"></textarea>
    <input type="radio" id="one" value="C" v-model="picked">
    <label for="AnswerC">IsCorrect</label>
    <br> 
    <textarea v-model="message" placeholder="Answer D"></textarea>
    <input type="radio" id="one" value="D" v-model="picked">
    <label for="AnswerD">IsCorrect</label>
    <br> 
    <button class="btn btn-primary" @click="addNewQuestion">SubmitQuestion</button>

<br>

<br>
  </div>
</template>

<script>

export default {
  name: "AdminPage",
  data() {
    return {
      picked:"",
      answerChoice:"",
      answerA:false,
      answerB:false,
      answerC:false,
      answerD:false,
      showForm:false,
      questionList: [],
    };
  },
  async created() {
    console.log("Composant QuestionForm page 'created'");
  },

  methods: {},
};
</script>

<style>
.QuestionForm {
  flex-wrap: wrap;
  flex-direction: column  ;
}
</style> 