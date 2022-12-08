from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

def find_password():
    website=website_entry.get()
    try:
        with open("data.json","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="No data",message="No data file found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Website: {website} \n Password: {password}")
        else:
            messagebox.showinfo(title="No website found", message="No data for that website found")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []
    password_letters=[choice(letters) for char in range(nr_letters)]
    password_symbols=[choice(symbols) for char in range(nr_symbols)]
    password_numbers=[choice(numbers) for char in range(nr_numbers)]
    password_list= password_letters+password_symbols+password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password) #copies it on clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()

    new_data= {
        website: {
            "email":email,
            "password":password

    }
    }
    if website =="" or password_entry.get()=="":
        messagebox.showinfo(title="Empty Entry",message="Please make sure you havent left any field empty")
    else:
       is_ok=messagebox.askokcancel(title=website,message=f"These are the details you entered:\nWebsite: {website}\nEmail : {email}\nPassword:{password}\n Is it okay to save inside your file?")
       if is_ok:
           try:
               with open("data.json", "r") as file:
                   #read old data
                   data=json.load(file)
                   #udpate old data with new_data
                   data.update(new_data)
           except FileNotFoundError:
               with open("data.json", "w") as file:
                   json.dump(new_data,file,indent=4)
           else:
               with open("data.json", "w") as file:
                   json.dump(data,file,indent=4)


       website_entry.delete(0, END)  # deleting the existing text in a current populated entry field
       password_entry.delete(0, END)
       messagebox.showinfo(title="Succesful",message="Yor data has been saved succesfully :)")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(bg="white",padx=50,pady=50)

canvas= Canvas(height=200, width=200,bg="white",highlightthickness=0)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)
website_label=Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
website_entry=Entry(bg="white", width=33)
website_entry.grid(row=1, column=1)
website_entry.focus() #adds the focus of cursor when  app opens

email_label=Label(text="Email/Username:",bg="white")
email_label.grid(row=2,column=0)
email_entry=Entry(bg="white",width=52)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"lisenpasha02@gmail.com")

password_label=Label(text="Password", bg="white")
password_label.grid(row=3, column=0)
password_entry=Entry(bg="white", width=33)
password_entry.grid(row=3, column=1)

generate_password=Button(text="Generate Password:",bg="white",fg="red",command=generate_password)
generate_password.grid(row=3,column=2)

search=Button(text="Search Password", bg="white", fg="red", command=find_password)
search.grid(row=1,column=2)

add_button=Button(text="Add",bg="white",fg="red",width=22,command=add)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()