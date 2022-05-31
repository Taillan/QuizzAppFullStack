import json
from multiprocessing.sharedctypes import Value
from flask import Flask, request
from werkzeug.exceptions import BadRequestKeyError
from jwt_utils import build_token, verify_token
from services.ParticipationServices import *
from services.QuestionServices import *
from errors import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": GetNumberQuestions(), "scores": [ p.toJSON() for p in GetAllParticipationService() ]}, 200

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
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	payload = request.get_json()

	try:
		NewQuestionService(payload)
		return QUESTION_CREATED_MESSAGE, 200
	except AlreadyExisting:
		return POSITION_ERROR_MESSAGE, 400
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500


@app.route('/questions', methods=['GET'])
def GetAllQuestion():
	try:
		questions = json.dumps([ q.toJSON() for q in GetAllQuestionService()])
		return questions, 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
	

@app.route('/questions/<int:question_position>', methods=['DELETE'])
def DelQuestion(question_position):
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	try:
		DeleteQuestionService(question_position)
		return QUESTION_DELETED_MESSAGE, 204
	except NotFound:
		return NOT_FOUND_MESSAGE , 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
	


@app.route('/questions/<int:position>', methods=['GET'])
def GetQuestion(position):
	try:
		result = GetQuestionService(position)
		return result.toJSON(), 200
	except NotFound :
		return NOT_FOUND_MESSAGE , 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500

@app.route('/questions/<int:position>', methods=['PUT'])
def UpdateQuestion(position):
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	payload = request.get_json()

	try:
		UpdateQuestionService(position, payload)
	except NotFound:
		return NOT_FOUND_MESSAGE, 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500
	return QUESTION_UPDATED_MESSAGE, 200

@app.route('/participations', methods=['POST'])
def NewParticipations():

	payload = request.get_json()

	try:
		participation = NewParticipationService(payload)
		return participation.toJSON(), 200
	except BadParticipation:
		return BAD_PARTICIPATION_MESSAGE, 400
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500

@app.route('/participations', methods=['DELETE'])
def DelAllParticipation():
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	try:
		DeleteAllParticipations()
		return ALLPARTICIPANT_DELETED_MESSAGE, 204
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 

if __name__ == "__main__":
	app.run()