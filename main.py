from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    not_valid = len(website) == 0 or len(email) == 0 or len(password) == 0
    if not_valid:
        messagebox.showwarning(title= "Oops", message= "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        
        if is_ok:
            with open("/Users/muhammadhamdazam/Documents/Python Programs/Day 29/password-manager-start/data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "xyz@gmail.com")
            password_entry.delete(0, END)
    


window = Tk()
window.title("My Password Manager")
window.config(padx= 20, pady=20)

canvas = Canvas(width=200, height=200)
photoimage = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= photoimage)
canvas.grid(row=0, column=1)


website_label = Label(text="Website: ")
email_label = Label(text="Email/Username: ")
password_label = Label(text="Password: ")


website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)


website_entry = Entry(width= 35)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "xyz@gmail.com")
password_entry = Entry(width= 18)


website_entry.grid(columnspan=2, row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)


generate_password_button = Button(text= "Generate Password", command= generate_password)
add_button = Button(text= "Add", width= 33, command= save)


generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan= 2)


window.mainloop()