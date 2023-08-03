# !/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
        return
    
    try:
        with open("data.json", "r") as data_file:
            # Reading existing data
            data = json.load(data_file)
            # Updating existing data
            data.update(new_data)
    except (FileNotFoundError, json.decoder.JSONDecodeError):    
        with open("data.json", "w") as data_file:
            # Saving initial data
            json.dump(new_data, data_file, indent=4)
    else:
        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
    finally:        
        entry_website.delete(0, tk.END)
        entry_password.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showwarning(title="No data saved", message="You do not have any data saved.")
    else:
        website = entry_website.get()        
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            search_result = f"Website: {website}\nUsername: {email}\nPassword: {password}"
            messagebox.showinfo(title=website, message=search_result)
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} found.")


# ------------------------------- UI SETUP --------------------------------- #
root = tk.Tk()
root.title("Password Manager")
root.config(padx=40, pady=30)

# create canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1, sticky='e')

label_email = tk.Label(text="Email/Username:")
label_email.grid(column=0, row=2, sticky='e')

label_password = tk.Label(root, text="Password:")
label_password.grid(column=0, row=3, sticky='e')

# Entries
entry_website = tk.Entry(root, width=30, bd=1)
entry_website.focus()
entry_website.grid(column=1, row=1, pady=3, padx=4, sticky='ew')

entry_email = tk.Entry(root, width=51)
entry_email.insert(0, "name@example.com")
entry_email.grid(column=1, row=2, columnspan=2, pady=2, padx=(4,0), sticky='ew')

entry_password = tk.Entry(root, width=30, bd=1)
entry_password.grid(column=1, row=3, pady=3, padx=4, sticky='ew')

# Buttons
button_generate_password = tk.Button(
    root, text="Generate Password", borderwidth=1, width=15, command=generate_password)
button_generate_password.grid(column=2, row=3, padx=0, pady=3, sticky='e')

button_Add = tk.Button(root, text="Add", width=43, borderwidth=1, command=save)
button_Add.grid(column=1, row=4, columnspan=2, pady=3, padx=(4,0), sticky='ew')

button_search = tk.Button(text="Search", borderwidth=1, width=15, command=find_password)
button_search.grid(column=2, row=1, sticky='ew')

# run app
root.mainloop()
