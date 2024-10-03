# This code is built upon a skeleton provided by App Brewery.
# Modifications and further implementations were done by Leandro.

import math
from tkinter import *
import os

# Get the current working directory
current_directory = os.path.join(os.getcwd(), "day 28 pomodoro timer")

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
tomato_sprite = os.path.join(current_directory, "pomodoro-start", "tomato.png")


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    label_timer.config(text="Timer", fg= GREEN)
    canvas.itemconfig(timer_set, text="00:00")
    b_start.config(state=NORMAL)
    checkmarks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    b_start.config(state=DISABLED)
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # long break --------------------- #
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)

    # work --------------------------- #
    elif reps % 2 == 1:
        label_timer.config(text="Work")
        count_down(work_sec)

    # short break -------------------- #
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes == 0:
        minutes = "00"
    elif minutes < 10:
        minutes = f"0{minutes}"

    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_set, text=f"{minutes}:{seconds}")

    # loop countdown ----------------------- #
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    # checkmark ---------------------------- #
    else:
        window.state("normal")
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        start_timer()
        format_check = ""
        n_of_check =math.floor ((reps % 8) / 2) # it restart from "" once it hit the long break
        for _ in range(n_of_check):
            format_check += "✔"
        checkmarks.config(text=format_check)



# ---------------------------- UI SETUP ------------------------------- #
# WINDOW ================================== #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# ======================================== #

# CANVAS ================================#
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=tomato_sprite)
canvas.create_image(100, 112, image=tomato_img)
timer_set = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)
# =========================================== #

# LABEL ===================================== #

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
label_timer.grid(column=1, row=0)

# =========================================== #

# START BUTTON ============================== #

b_start = Button(text="Start", command=start_timer, bg= "white", highlightthickness=0)

b_start.grid(column=0, row=2)

# =========================================== #

# RESET BUTTON ============================== #
b_restart = Button(text="Restart", bg= "white", command=reset_timer, highlightthickness=0)
b_restart.grid(column=2, row=2)
# =========================================== #

# CHECKMARK ================================= #
checkmarks= Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

# =========================================== #


window.mainloop()
