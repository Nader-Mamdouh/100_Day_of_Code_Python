from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR, highlightthickness=0)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="Start", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_label = Label(text=f"Score : 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_label.grid(row=0, column=0)

        self.true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=1)
        self.wrong_image = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=self.wrong_image, highlightthickness=0, command=self.false_pressed)
        self.button_wrong.grid(row=2, column=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=q_text)

        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of Questions.")
            self.button_true.config(state="disabled")
            self.button_wrong.config(state="disabled")
        self.canvas.config(bg="white")

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        q_answer = self.quiz.check_answer("False")
        self.feedback(q_answer)

    def feedback(self, right):
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
