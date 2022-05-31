import json
import sqlite3
from flask import Flask, request
from jwt_utils import build_token, verify_token
from services.QuestionServices import NewQuestionService, GetQuestionService,DeleteQuestionService,UpdateQuestionService

app = Flask(__name__)

def get_db_connection():
	conn = sqlite3.connect('database.db')
	return conn

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	try:
		password = payload['password']
	except:
		return "Not a JSON body, or missing password field", 500

	if password == "Vive l'ESIEE !":
		response = {"token": build_token()}
		return json.dumps(response), 200
	else:
		return "Wrong password", 401

@app.route('/questions', methods=['POST'])
def NewQuestion():
	payload = request.get_json()
	if verify_token(request.headers.get('Authorization')):
		NewQuestionService(payload)
		return "Created", 200
	else:
		return "Wrong token", 401

@app.route('/questions/<int:question_id>', methods=['DELETE'])
def DelQuestion(question_id):
	if verify_token(request.headers.get('Authorization')):
		DeleteQuestionService(question_id)
		return "Deleted", 201
	else:
		return "Wrong token", 401

@app.route('/questions/<int:question_id>', methods=['GET'])
def GetQuestion(question_id):
	try:
		result = GetQuestionService(question_id)
		return result.toJSON(), 200
	except ValueError:
		return ValueError , 404
	return "test", 200

@app.route('/questions/<int:question_id>', methods=['PUT'])
def UpdateQuestion(question_id):
	payload = request.get_json()
	if verify_token(request.headers.get('Authorization')):
		UpdateQuestionService(payload)
		return "Updated", 200
	else:
		return "Wrong token", 401


if __name__ == "__main__":
	app.run(ssl_context='adhoc')