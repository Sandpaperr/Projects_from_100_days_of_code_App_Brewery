import tkinter as t
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
import os

FILE_LOGO = os.path.join(os.getcwd(), "day 29 password keeper", "password-manager-start", "logo.png")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    password_entry.delete(0, t.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    if len(website) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave website field empty when searching!")
    else:
        try:
            with open("data.jason", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No datafile found")
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                pyperclip.copy(password)
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\n\n "
                                                           f"Password saved to clipboard")
            else:
                messagebox.showwarning(title="Oops", message=f"{website} is not present in the database")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().title()
    username = username_entry.get()
    chosen_password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": chosen_password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(chosen_password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.jason", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.jason", "w") as file:
                json.dump(new_data, file, indent=4)

        else:

            data.update(new_data)
            with open("data.jason", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, t.END)
            password_entry.delete(0, t.END)


# ---------------------------- UI SETUP ------------------------------- #

# MAIN WINDOW ======================= #
window = t.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# =================================== #

# IMAGE ============================= #
canvas = t.Canvas(width=200, height=200)
image_pass = t.PhotoImage(file=FILE_LOGO)
canvas.create_image(100, 100, image=image_pass)
canvas.grid(row=0, column=1)

# =================================== #

# Labels
website_label = t.Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = t.Label(text="Email/Username")
username_label.grid(row=2, column=0)
password_label = t.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = t.Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()
username_entry = t.Entry(width=51)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "leandrorussoooo@gmail.com")
password_entry = t.Entry(width=33)
password_entry.grid(column=1, row=3, padx=0, pady=0)
#
# Buttons

password_button = t.Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(column=2, row=3)

add_button = t.Button(text="Add", width=43, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = t.Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
