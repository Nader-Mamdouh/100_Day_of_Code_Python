from tkinter import *
window = Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=150, height=100)
data = Entry(width=10)
data.grid(row=0, column=1)

my_label1 = Label(text="is equal to ")
my_label1.grid(row=1, column=0)
my_label2 = Label(text=" Miles ")
my_label2.grid(row=0, column=2)
my_label3 = Label(text=" 0 ")
my_label3.grid(row=1, column=1)
my_label4 = Label(text=" KM ")
my_label4.grid(row=1, column=2)


def button_clicked():
    new_text = int(data.get())*1.6
    my_label3.config(text=new_text)


my_button = Button(text="calculate", command=button_clicked)
my_button.grid(row=3, column=1)


window.mainloop()
