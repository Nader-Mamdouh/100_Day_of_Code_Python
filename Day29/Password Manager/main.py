from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_pass.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askokcancel(message="Make sure you have not left any fields empty. ")
    else:
        is_ok = messagebox.askokcancel(message="Are you sure?")
        if is_ok:
            with open("Password_Manager.txt", "w") as file:
                file.write(website + " | " + email + " | " + password + "\n")


        input_website.delete(0, END)
        input_pass.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(width=400, height=400)
window.config(padx=50, pady=50)
window.title("Password Manager")
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username :")
email_label.grid(row=2, column=0)
password_label = Label(text="Password :")
password_label.grid(row=3, column=0)

#input

input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_pass = Entry(width=21)
input_pass.grid(row=3, column=1, columnspan=1)


#Buttons

generate_button = Button(text="Generate Button", width=14,command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
