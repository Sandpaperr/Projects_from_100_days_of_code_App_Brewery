from tkinter import *


def button_clicked():
    print("You clicked me")


window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx= 20, pady= 20)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = Button(text="New click me", command= button_clicked)
new_button.grid(column= 2, row= 0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
