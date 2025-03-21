from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text= "Timer")
    reps = 0
    progress_check.config(text= "")
    canvas.itemconfig(timer_text, text= "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text= "Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text= "Break", fg= PINK)
    else:
        count_down(work_sec)
        timer_label.config(text= "Work", fg= YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer

    check_mark = "✔"
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(50, count_down, count - 1)

    else:
        start_timer()
        progress_check.config(text= f"{check_mark * (reps // 2)}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= GREEN)

canvas = Canvas(width= 200, height= 224, bg= GREEN, highlightthickness= 0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image= tomato_img)                            # x co-ord, y co-ord, image
timer_text = canvas.create_text(100, 130, text= "00:00", fill= "white", font= (FONT_NAME, 32, "normal"))
canvas.grid(column= 1, row= 1)

timer_label = Label(text= "Timer", fg= RED, bg= GREEN, font= (FONT_NAME, 38, "normal"))
timer_label.grid(column= 1, row= 0)

start_button = Button(text= "Start", font= (FONT_NAME, 24, "normal"), highlightthickness= 0, command= start_timer)
start_button.grid(column= 0, row= 2)

stop_button = Button(text= "Reset", font= (FONT_NAME, 24, "normal"), highlightthickness= 0, command= reset_timer)
stop_button.grid(column= 2, row= 2)

progress_check = Label(bg= GREEN, fg= RED, font= (FONT_NAME, 38, "normal"))
progress_check.grid(column= 1, row= 2)

window.mainloop()