from tkinter import *


def calculate():
    miles = float(miles_input.get())
    km = int(miles * 1.609)
    km_result_label.config(text=str(km))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=14)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_result_label = Label()
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

converter_button = Button(text="Calculate", command=calculate)
converter_button.grid(row=2, column=1)


window.mainloop()
