from xmlrpc.client import boolean
import json

class PossibleAnswers():
	def __init__(self, text: str, isCorrect: bool):
		self.text = text
		self.isCorrect = isCorrect
	
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

class Question():
	def __init__(self, title: str, text: str, position: int, image: str, possibleAnswers: PossibleAnswers=[]):
		self.title = title
		self.text = text
		self.position = position
		self.image = image	
		self.possibleAnswers = possibleAnswers
	
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)