import json

class PossibleAnswers():
    def __init__(self, text: str, isCorrect: bool):
        self.text = text
        self.isCorrect = isCorrect
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
