import tkinter as t
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# -------------CREATE FLASH CARD------------- #
try:
    data_csv = pandas.read_csv(r"day 31 flash cards\flash-card-project-start\data\words_to_learn.csv")
except FileNotFoundError:
    data_csv = pandas.read_csv(r"day 31 flash cards\flash-card-project-start\data\spanish_english.csv")
finally:
    to_learn = data_csv.to_dict(orient="records")
    current_card = {}


def next_flash_card():
    global current_card, flip_timer
    current_card = choice(to_learn)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(word, text=current_card["Spanish"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_flash_card()


# ------------------- UI -------------------- #
window = t.Tk()
window.title("Spanish flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# CANVAS ==================================== #
canvas = t.Canvas(width=810, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = t.PhotoImage(file=r"./day 31 flash cards\flash-card-project-start\images\card_front.png")
card_back = t.PhotoImage(file=r"./day 31 flash cards\flash-card-project-start\images\card_back.png")

card_image = canvas.create_image(405, 275, image=card_front)
language = canvas.create_text(405, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(405, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

# BUTTONS =================================== #

wrong_image = t.PhotoImage(file=r"./day 31 flash cards\flash-card-project-start\images\wrong.png")
right_image = t.PhotoImage(file=r"./day 31 flash cards\flash-card-project-start\images\right.png")

wrong_button = t.Button(image=wrong_image, highlightthickness=0, command=next_flash_card)
wrong_button.grid(column=0, row=1)

right_button = t.Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_flash_card()

window.mainloop()
