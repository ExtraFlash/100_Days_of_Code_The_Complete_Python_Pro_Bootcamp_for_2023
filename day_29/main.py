from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if website.strip() == "" or email.strip() == "" or password.strip() == "":
        messagebox.showerror(title="Oops", message="One of the fields is empty, please fill.")
        return

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open("data.json", "w") as file:
            data.update(new_data)
            json.dump(data, file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            message = f"Email: {email}\nPassword: {password}"
            messagebox.showinfo(title=website, message=message)
        else:
            messagebox.showerror(title="Oops", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=51)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'orshkuri2000@gmail.com')
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, highlightthickness=0, command=search)
search_button.grid(row=1, column=2)
gen_password_button = Button(text="Generate Password", width=15, highlightthickness=0, command=generate_password)
gen_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
