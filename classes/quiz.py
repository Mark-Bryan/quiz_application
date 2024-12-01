import tkinter as tk


class Quiz:

    def __init__(self, Id, name, description, finalScore, questions, responses):
        self.Id = Id
        self.name = name
        self.description = description
        self.finalScore = finalScore
        self.questions = questions
        self.responses = responses

    def checkAnswer(self, question_index, selected_answer):
        correct_answer = self.questions[question_index]["answer"]
        if selected_answer == correct_answer:
            self.finalScore += 1
            return True, "Correct"
        else:
            return False, f"Incorrect option, The correct answer was : {correct_answer}"

    def getResults(self):
        return self.finalScore, len(self.questions)

    def save(self, username):
        if username and len(username.strip()) > 0:
            with open("quiz_results.txt", "a") as f:
                f.write(f"{username}: {self.finalScore}/{len(self.questions)}\n")

    def getResultsForUser(self, username):
        if username.strip() and Quiz.results_file_exists():
            with open("quiz_results.txt", "r") as f:
                lines = f.readlines()
                return [line.strip() for line in lines if line.startswith(username)]
            return []
