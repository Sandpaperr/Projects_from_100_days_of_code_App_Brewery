from tkinter import *


def miles_to_kilometer():
    miles = float(miles_input.get())
    km = miles *1.609
    result_label.config(text= f"{km}")

window = Tk()

window.title("Mile to Km Converter")
window.config(padx= 20, pady= 20)

# Miles
miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

# Km
km = Label (text= "Km")
km.grid(column= 2, row= 1)

# Is equal to
equal_to = Label(text= "is equal to")
equal_to.grid(column= 0, row= 1)

# result label
result_label = Label(text= "0")
result_label.grid(column= 1, row= 1)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Calculate
new_button = Button(text="Calculate", command= miles_to_kilometer)
new_button.grid(column= 1, row= 3)

window.mainloop()
