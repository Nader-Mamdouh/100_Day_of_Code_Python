from tkinter import *
import pandas
import random
current_card = {}
data = {}

#----------------------------------------------get word----------------------------------------------------------------#

try:
    file1 = pandas.read_csv("Words_to_learn.csv")
except FileNotFoundError:
    file2 = pandas.read_csv("french_words.csv.csv.csv")
    data = file2.to_dict(orient="records")
else:
    data = file1.to_dict(orient="records")


def Next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(Background_image, image=front_image)
    flip_timer = window.after(3000, func=Flip_card)


def Flip_card():
    canvas.itemconfig(Background_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    data.remove(current_card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("Words_to_learn.csv", index=False)
    Next_card()
#----------------------------------------------------UI----------------------------------------------------------------#


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
flip_timer = window.after(3000, func=Flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

#Image
front_image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
Background_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

#Buttons
true_image = PhotoImage(file="right.png")
button_true = Button(image=true_image, highlightthickness=0, command=is_known)
button_true.grid(row=1, column=1)
wrong_image = PhotoImage(file="wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=Next_card)
button_wrong.grid(row=1, column=0)
Next_card()


window.mainloop()



