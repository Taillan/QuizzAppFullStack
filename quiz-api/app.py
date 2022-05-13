from flask import Flask, request
from jwt_utils import build_token, decode_token

app = Flask(__name__)

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
		return build_token(), 200
	else:
		return "Wrong password", 401

if __name__ == "__main__":
    app.run(ssl_context='adhoc')