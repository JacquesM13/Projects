from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR, padx= 20, pady= 20)

        self.score = 0
        self.score_label = Label(text= f"Score: {self.score}", bg= THEME_COLOR, fg= "white")
        self.score_label.grid(column= 1, row= 0)

        self.canvas = Canvas(width= 300, height = 250, bg= "white", highlightthickness= 0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width= 280,
                                                     text="Question Text",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)

        self.canvas.grid(column= 0, row= 1, columnspan= 2, pady= 30)

        self.true_img = PhotoImage(file= "images/true.png")
        self.true_button = Button(image= self.true_img, highlightthickness= 0, command= self.check_true)
        self.true_button.grid(column= 1, row= 2)

        self.false_img = PhotoImage(file= "images/false.png")
        self.false_button = Button(image= self.false_img, highlightthickness= 0, command= self.check_false)
        self.false_button.grid(column= 0, row= 2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You've finished the quiz!")
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(1000, self.get_next_question)
