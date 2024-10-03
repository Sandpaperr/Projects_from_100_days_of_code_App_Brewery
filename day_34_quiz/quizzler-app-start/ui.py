THEME_COLOR = "#375362"
import tkinter as t
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = t.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_image= t.PhotoImage(file=r"./day_34_quiz\quizzler-app-start\images\true.png")
        self.check_button = t.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(column=0, row=2)

        false_image= t.PhotoImage(file=r"./day_34_quiz\quizzler-app-start\images\false.png")
        self.cross_button = t.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(column=1, row=2)

        self.score = 0
        self.score_text = t.Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.canvas = t.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, fill="black", text="aa", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def update_score(self):
        self.score += 1
        self.canvas.itemconfig(self.question_text, text=f"Score: {self.score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)