<template>
  <div class="QuestionForm">
    <label for="title">title</label>
    <br>
    <input type="Username" placeholder="title" v-model="title" />
    <br>
    <label for="position">position</label>
    <br>
    <input type="position" placeholder="position" v-model="position" />
    <br>
    <label for="text">text</label>
    <br>
    <textarea v-model="text" placeholder="text"></textarea>
    <br>
    <label for="AnswerA">Answer A</label>
    <br>
    <textarea v-model="textA" placeholder="Answer A"></textarea>
    <input type="radio" id="one" value="A" v-model="picked" @click="answerA=true;answerB=false;answerC=false;answerD=false">
    <label for="AnswerA">IsCorrect</label>
    <br> 
    <label for="AnswerB">Answer B</label>
    <br>
    <textarea v-model="textB" placeholder="Answer B"></textarea>
    <input type="radio" id="one" value="B" v-model="picked" @click="answerA=false;answerB=true;answerC=false;answerD=false">
    <label for="AnswerB">IsCorrect</label>
    <br> 
    <label for="AnswerC">Answer C</label>
    <br>
    <textarea v-model="textC" placeholder="Answer C"></textarea>
    <input type="radio" id="one" value="C" v-model="picked" @click="answerA=false;answerB=false;answerC=true;answerD=false">
    <label for="AnswerC">IsCorrect</label>
    <br> 
    <label for="AnswerD">Answer D</label>
    <br>
    <textarea v-model="textD" placeholder="Answer D"></textarea>
    <input type="radio" id="one" value="D" v-model="picked" @click="answerA=false;answerB=false;answerC=false;answerD=true">
    <label for="AnswerD" >IsCorrect</label>    
    <br>
    <ImageUpload @file-change="imageChange"/> 
    <img v-if="this.image" :src="this.image" />
    <br> 
    <button class="btn btn-primary" @click="$emit('form-completed', this.text,this.title,this.image,this.position,this.textA,this.answerA,this.textB,this.answerB,this.textC,this.answerC,this.textD,this.answerD)">{{actionForm}}</button>

  </div>
</template>

<script>
import ImageUpload from "@/components/ImageUpload.vue";

export default {
  name: "QuestionForm",
  emits: ["form-completed"],
  props: {
    actionForm: String,
  },
  components: {
    ImageUpload: ImageUpload,
  },
  data() {
    return {
      picked:"",
      answerChoice:"",
      title:"",
      position:"",
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
    };
  },
  async created() {
    console.log("Composant QuestionForm page 'created'");
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