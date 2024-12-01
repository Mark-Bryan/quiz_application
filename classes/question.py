class Question:

    def __init__(self, Id, description, responses, answer):
        self.Id = Id
        self.description = description
        self.responses = responses
        self.answer = answer

    def save(self):
        return True

    def checkAnswer(self):
        return True
