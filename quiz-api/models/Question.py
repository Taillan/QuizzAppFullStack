import json
from models.PossibleAnswers import PossibleAnswers

class Question():
    def __init__(self, title: str, text: str, position: int, image: str, possibleAnswers: PossibleAnswers=[]):
        self.title = title
        self.text = text
        self.position = position
        self.image = image	
        self.possibleAnswers = possibleAnswers
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)