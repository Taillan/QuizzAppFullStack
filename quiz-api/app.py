import json
from multiprocessing.sharedctypes import Value
from flask import Flask, request
from jwt_utils import build_token, verify_token
from services.QuestionServices import NewQuestionService, GetQuestionService,DeleteQuestionService,UpdateQuestionService, GetAllQuestionService
from errors import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()

	try:
		password = payload['password']
	except:
		return BAD_REQUEST_PASSWORD_MESSAGE, 400

	if password == "Vive l'ESIEE !":
		response = {"token": build_token()}
		return json.dumps(response), 200
	else:
		return WRONG_PASSWORD_MESSAGE, 401

@app.route('/questions', methods=['POST'])
def NewQuestion():
	if not verify_token(request.headers.get('Authorization')):
		return BAD_TOKEN_MESSAGE, 401

	payload = request.get_json()

	try:
		NewQuestionService(payload)
		return QUESTION_CREATED_MESSAGE, 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500


@app.route('/questions', methods=['GET'])
def GetAllQuestion():
	try:
		questions = json.dumps([ q.toJSON() for q in GetAllQuestionService()])
		return questions, 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
	

@app.route('/questions/<int:question_id>', methods=['DELETE'])
def DelQuestion(question_id):
	if not verify_token(request.headers.get('Authorization')):
		return BAD_TOKEN_MESSAGE, 401

	try:
		DeleteQuestionService(question_id)
		return QUESTION_DELETED_MESSAGE, 204
	except NotFound:
		return NOT_FOUND_MESSAGE , 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
	


@app.route('/questions/<int:question_id>', methods=['GET'])
def GetQuestion(question_id):
	try:
		result = GetQuestionService(question_id)
		return result.toJSON(), 200
	except NotFound :
		return NOT_FOUND_MESSAGE , 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500

@app.route('/questions/<int:question_id>', methods=['PUT'])
def UpdateQuestion(question_id):
	if not verify_token(request.headers.get('Authorization')):
		return BAD_TOKEN_MESSAGE, 401

	payload = request.get_json()

	try:
		UpdateQuestionService(question_id, payload)
	except NotFound:
		return NOT_FOUND_MESSAGE, 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500
	return QUESTION_UPDATED_MESSAGE, 200

if __name__ == "__main__":
	app.run()