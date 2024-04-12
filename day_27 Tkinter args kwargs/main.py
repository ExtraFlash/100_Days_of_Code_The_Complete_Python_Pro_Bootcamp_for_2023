from tkinter import *


# Button
def button_clicked():
    text = my_input.get()
    my_label.config(text=text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
my_input = Entry(width=14)
my_input.grid(column=3, row=2)

# Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)


window.mainloop()
