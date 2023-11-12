from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    reset_status_button()
    reset_time()
    global reps
    reps = 0
    checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        get_long_break()
        count_down(long_break)
    elif reps % 2 == 0:
        count_down(short_break)
        get_short_break()
    else :
        get_start()
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if  int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=100)
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


def get_start():
    status_label.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)


def get_short_break():
    status_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW, highlightthickness=0)


def get_long_break():
    status_label.config(text="Long Break", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW, highlightthickness=0)


def reset_status_button():
    status_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)


def reset_time():
    canvas.itemconfig(timer_text, text="00:00")


status_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
status_label.grid(column=1, row=0)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=2)
checkmark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark.grid(column=1, row=3)
window.mainloop()
