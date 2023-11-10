# program that will convert miles to km
from tkinter import *

window = Tk()
window.title("Miles to km convertor")
window.minsize(width=200, height=100)
window.config(pady=20, padx=20)

def convert_miles():
    miles = float(entry.get())
    kilometers = miles * 1.60934
    my_lable3.config(text=kilometers)


entry = Entry(width=10)
entry.grid(column=1, row=0)

my_lable1 = Label(text="Miles")
my_lable1.grid(column=2, row=0)

my_lable2 = Label(text="is equal to")
my_lable2.grid(column=0, row=1)

my_lable3 = Label(text="0")
my_lable3.grid(column=1, row=1)

my_lable4 = Label(text="Km")
my_lable4.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=convert_miles)
calculate_button.grid(column=1, row=3)

window.mainloop()
