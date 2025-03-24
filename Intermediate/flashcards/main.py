from tkinter import *
import pandas
import random
import time

to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")

else:
    to_learn = data.to_dict(orient= "records")

current_card = {}
learnt_words = {}

BACKGROUND_COLOR = "#B1DDC6"

def update_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text= "French", fill= "black")
    canvas.itemconfig(word_text, text= current_card["French"], fill= "black")
    canvas.itemconfig(card_img, image= card_front)
    flip_timer = window.after(3000, func= flip_card)

def learnt():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    update_card()

def flip_card():
    canvas.itemconfig(card_img, image= card_back)
    canvas.itemconfig(lang_text, text= "English", fill= "white")
    canvas.itemconfig(word_text, text= current_card["English"], fill= "white")

window = Tk()
window.title("Flashy")
window.config(bg= BACKGROUND_COLOR, padx= 50, pady= 50)

canvas = Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_front = PhotoImage(file= "images/card_front.png")
card_back = PhotoImage(file= "images/card_back.png")
card_img = canvas.create_image(400, 263, image= card_front)
canvas.grid(column= 0, row= 0, columnspan= 2)
lang_text = canvas.create_text(400, 150, text= "Title", fill= "black", font= ("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text= "Word", fill= "black", font= ("Ariel", 60, "bold"))

tick_img = PhotoImage(file= "images/right.png")
tick_button = Button(image= tick_img, highlightthickness= 0, command= learnt)
tick_button.grid(column= 1, row= 1)

cross_img = PhotoImage(file= "images/wrong.png")
cross_button = Button(image= cross_img, highlightthickness= 0, command= update_card)
cross_button.grid(column= 0, row= 1)

flip_timer = window.after(3000, func= flip_card)

update_card()

window.mainloop()