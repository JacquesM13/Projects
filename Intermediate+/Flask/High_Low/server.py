from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)

@app.route("/")
def home_page():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src= "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjFhYjl6YTR5a244dWJwYXJ4OHFvdzNkc2JibzVvN2M3ZjhzczJxbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PVkTqqgKOUGORnINJy/giphy.gif">')

@app.route("/<int:number>")
def number_page(number):
    if number > random_number:
        return (f"<h1 style= 'color: red'>You guessed {number}, that's too high</h1>"
                f"<img src= 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmt0cDJsNDMyb3kzcnNoYXVya3N4aWRxdjUzMGhtemphMHpiNnVqdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DMNqE0oBP2BEY/giphy.gif' width= 500px>")
    elif number < random_number:
        return (f"<h1 style= 'color: blue'>You guessed {number}, that's too low</h1>"
                f"<img src= 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXFhMG43YXNmbnM4ang5dmdmZG0wZHhkN2owbW90eDIzNjJsZTE5MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.gif' width= 500px>")
    else:
        return (f"<h1 style= 'color: green'>You guessed {number}, that's correct!</h1>"
                f"<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3ZyYno5bmY3YnQwYmRrMW1jM2hqbnNld3lyZ2JmajZkYmNkZGdvMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7abKhOpu0NwenH3O/giphy.gif' width= 500px>")

if __name__ == "__main__":
    # Run in debug mode to auto-reload
    app.run(debug= True)
