<template>
  <div class="QuestionForm">
    <label for="title">title</label>
    <br>
    <input type="Username" placeholder="title" v-model="title" />
    <br>
    <label for="position">position</label>
    <br>
    <input type="position" placeholder="position" v-model="pose" />
    <br>
    <label for="text">text</label>
    <br>
    <textarea v-model="text" placeholder="text"></textarea>
    <br>
    <label for="AnswerA">Answer A</label>
    <br>
    <textarea v-model="textA" placeholder="Answer A"></textarea>
    <input type="radio" id="one" value="A" :checked="answerA" v-model="picked" @click="answerA=true;answerB=false;answerC=false;answerD=false">
    <label for="AnswerA">IsCorrect</label>
    <br> 
    <label for="AnswerB">Answer B</label>
    <br>
    <textarea v-model="textB" placeholder="Answer B"></textarea>
    <input type="radio" id="one" value="B" :checked="answerB" v-model="picked" @click="answerA=false;answerB=true;answerC=false;answerD=false">
    <label for="AnswerB">IsCorrect</label>
    <br> 
    <label for="AnswerC">Answer C</label>
    <br>
    <textarea v-model="textC" placeholder="Answer C"></textarea>
    <input type="radio" id="one" value="C" :checked="answerC" v-model="picked" @click="answerA=false;answerB=false;answerC=true;answerD=false">
    <label for="AnswerC">IsCorrect</label>
    <br> 
    <label for="AnswerD">Answer D</label>
    <br>
    <textarea v-model="textD" placeholder="Answer D"></textarea>
    <input type="radio" id="one" value="D" :checked="answerD" v-model="picked" @click="answerA=false;answerB=false;answerC=false;answerD=true">
    <label for="AnswerD" >IsCorrect</label>    
    <br>
    <ImageUpload @file-change="imageChange"/> 
    <img v-if="this.image" :src="this.image" />
    <br> 
    <button class="btn btn-primary" @click="$emit('form-completed', this.text,this.title,this.image,this.pose,this.textA,this.answerA,this.textB,this.answerB,this.textC,this.answerC,this.textD,this.answerD)">{{actionForm}}</button>

  </div>
</template>

<script>
import ImageUpload from "@/components/ImageUpload.vue";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "QuestionForm",
  emits: ["form-completed"],
  props: {
    actionForm: String,
    position:Number
  },
  components: {
    ImageUpload: ImageUpload,
  },
  data() {
    return {
      picked:"",
      pose:null,
      answerChoice:"",
      title:"",
      textA:"",
      textB:"",
      textC:"",
      textD:"",
      text:"",
      image:"falseb64imagecontent",
      answerA:false,
      answerB:false,
      answerC:false,
      answerD:false,
      showForm:false,
      questionList: [],
      question: {},
    };
  },
  async created() {
    console.log("Composant QuestionForm page 'created'");
    this.pose = this.position;
    if(this.position){
     let tempQuestion = await quizApiService.getQuestionByPosition(this.position);
      this.question = tempQuestion.data;
      this.title = this.question.title;
      this.textA = this.question.possibleAnswers[0].text;
      this.textB = this.question.possibleAnswers[1].text;
      this.textC = this.question.possibleAnswers[2].text;
      this.textD = this.question.possibleAnswers[3].text;
      this.text = this.question.text;
      this.image = this.question.image;
      this.answerA = this.question.possibleAnswers[0].isCorrect;
      this.answerB = this.question.possibleAnswers[1].isCorrect;
      this.answerC = this.question.possibleAnswers[2].isCorrect;
      this.answerD = this.question.possibleAnswers[3].isCorrect;
    }
  },

  methods: {
    imageChange(dataUrl){
      if(dataUrl)this.image=dataUrl;
      else{this.image="falseb64imagecontent";}
      console.log(dataUrl," ",this.image);
    }
  },
};
</script>

<style>
.QuestionForm {
  flex-wrap: wrap;
  flex-direction: column  ;
}
</style> 