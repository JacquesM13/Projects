from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(3, 5))]
    password_list += [choice(numbers) for _ in range(randint(3, 5))]

    shuffle(password_list)
    random_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else:
        with open("data.json", "w") as data_file:
            print("Code works up to here")
            json.dump(new_data, data_file, indent= 4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0, END)

        website_entry.focus()
        email_entry.insert(0, "an_email@hotmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
# window.minsize(width=250, height=250)
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# --------------------- WEBSITE -------------------------
# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Entry
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# --------------------- EMAIL/USERNAME ----------------------------
# Label
email_label = Label(text="Email/Username:")
email_label.grid(column= 0, row= 2)
# Entry
email_entry = Entry(width= 35, bg= "white", fg= "black", highlightthickness= 0)
email_entry.grid(column= 1, row= 2, columnspan= 2, sticky= "EW")
email_entry.insert(0, "jacquesmassi@gmail.com")

# --------------------- PASSWORD --------------------------
# Label
password_label = Label(text= "Password:", bg= "white", fg= "black")
password_label.grid(column= 0, row= 3)
# Entry
password_entry = Entry(width= 21, bg= "white", fg= "black", highlightthickness= 0)
password_entry.grid(column= 1, row= 3, sticky= "EW")
# Button
password_button = Button(text= "Generate Password", highlightthickness= 0, command= generate_password)
password_button.grid(column= 2, row= 3, sticky= "EW")

# ---------------------- ADD --------------------------
# Button
add_button = Button(text= "Add", highlightthickness= 0, width= 36, command= save)
add_button.grid(column= 1, row= 4, columnspan= 2, sticky= "EW")

window.mainloop()