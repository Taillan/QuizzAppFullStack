import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    // not implemented
  },

  getQuizInfo() {
    console.debug("GetRegistredScore");
    var quizInfo = this.call("GET", "quiz-info");
    return quizInfo;
  },

  getQuestionByPosition: function (position) {
    console.debug("getQuestionByPosition position:" + position);
    var question = this.call("GET", "questions/" + position);
    return question;
  }
};