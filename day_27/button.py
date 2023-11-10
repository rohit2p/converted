# using tkinter module to crate a button on the screen that will print "button clicked"
from tkinter import *

window = Tk()
window.title("button")
window.minsize(width=500, height=300)

# creating an entry table using tkinter module
input = Entry(width=10)
input.pack()
print(input.get())

# button
def button_clicked():
    my_lable = Label(text="new_text", font=("Arial", 24, "bold"))
    new_text = input.get()  # get() this function returns the entry string
    my_lable.config(text=new_text)
    my_lable.pack()


button = Button(window, text="Click me", command=button_clicked)
button.pack()

window.mainloop()

"""In this example, we define a function button_clicked() that will be called when the button is clicked. 
The Button() function creates a button widget with the given text and command.
The command parameter specifies the function to be executed when the button is clicked. 
Finally, we use the pack() method to add the button to the window, and mainloop() starts the main event loop of the window."""
