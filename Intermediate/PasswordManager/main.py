import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            # print(data)
    except FileNotFoundError:
        messagebox.showinfo(title= "Details not found", message= "No details for the website exist")

    else:
        if web_entry.get() in data:
            data = data[web_entry.get()]
            email = data['email']
            password = data['password']
            messagebox.showinfo(title= "Details", message=f"{web_entry.get()}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title= "Details not found", message= "No details for the website exist")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    if len(web_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showerror(title= "Oops", message= "Please leave no field empty")

    else:
        website = web_entry.get()
        email = email_user_entry.get()
        password_data = pass_entry.get()
        new_data = {
            website: {
                "email": email,
                "password": password_data,
            }
        }
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Uploading new data
                json.dump(data, data_file, indent=4)

        finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50, bg= "white")

# Row 0
canvas = Canvas(width= 200, height= 200, bg= "white", highlightthickness= 0)
lock_img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= lock_img)
canvas.grid(column= 1, row= 0)

# Row 1
web_label = Label(text= "Website:", bg= "white", fg= "black")
web_label.grid(column= 0, row= 1)

web_entry = Entry(bg= "white", fg= "black", highlightthickness= 0)
web_entry.grid(column= 1, row= 1, sticky= "EW")
web_entry.focus()

search_button = Button(text= "Search", highlightthickness= 0, command= find_password)
search_button.grid(column= 2, row= 1, sticky= "EW")

# Row 2
email_user_label = Label(text= "Email/Username:", bg= "white", fg= "black")
email_user_label.grid(column= 0, row= 2)

email_user_entry = Entry(width= 35, bg= "white", fg= "black", highlightthickness= 0)
email_user_entry.grid(column= 1, row= 2, columnspan= 2, sticky= "EW")
email_user_entry.insert(0, "jacquesmassi@gmail.com")

# Row 3
pass_label = Label(text= "Password:", bg= "white", fg= "black")
pass_label.grid(column= 0, row= 3)

pass_entry = Entry(width= 21, bg= "white", fg= "black", highlightthickness= 0)
pass_entry.grid(column= 1, row= 3, sticky= "EW")

gen_button = Button(text= "Generate Password", highlightthickness= 0, command= generate_password)
gen_button.grid(column= 2, row= 3, sticky= "EW")

# Row 4
add_button = Button(text= "Add", highlightthickness= 0, width= 36, command= add_password, bg= "white")
add_button.grid(column= 1, row= 4, columnspan= 2, sticky= "EW")

window.mainloop()