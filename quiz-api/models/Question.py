import json

class Question():
    def __init__(self, title: str, text: str, position: int, image: str,  question_id: int=None):
        self.id = question_id
        self.title = title
        self.text = text
        self.position = position
        self.image = image	
        self.possibleAnswers = []
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)