from tkinter import *
from tkinter import messagebox, simpledialog
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(4, 8))]
    password_chars =[choice(symbols) for _ in range(randint(2, 4))]
    password_nums =[choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_letters+password_chars+password_nums
    shuffle(password_list)

    password = "".join(password_list)

    PasswordWindow.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=WebsiteWindow.get()
    email=EmailWindow.get()
    password=PasswordWindow.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Warning", message=" Please make sure you haven't \n left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                WebsiteWindow.delete(0, END)
                PasswordWindow.delete(0, END)
                OUTPUT=Label(text="Information saved", bg="black", fg="green")
                OUTPUT.grid(column=8, row=34, columnspan=3)


def find():
    website=WebsiteWindow.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            if website in data:
                email=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title="Password saved to clipboard", message=f" {website} \n Login: {email}\n Password: {password}")
                pyperclip.copy(password)
                messagebox.button(title)
    except FileNotFoundError:
            all_websites = data.keys()
            all_webs_clean = (', \n \n '.join(all_websites))
            messagebox.showinfo("Search results", message=f"  No details for { website } exist. \n  Available in the directory: \n \n {all_webs_clean}")
    else:
            all_websites = data.keys()
            all_webs_clean = (', \n \n '.join(all_websites))
            messagebox.showinfo("Search results", message=f"  No details for { website } exist. \n  Available in the directory: \n \n {all_webs_clean}")
            ws.destroy()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Locksmith ///")
window.config(padx=50, pady=50, bg="black")

canvas = Canvas (width=250, height=250, background="black", highlightthickness=0)
image=PhotoImage(file="logo.png")
canvas.create_image(90,100, image=image)

canvas.grid(column=10, row=20)


WEBSITE=Label(text="WEBSITE", bg="black", fg="#545454" )
WEBSITE.grid(column=8, row=22,columnspan=1)
WebsiteWindow=Entry(width=24)
WebsiteWindow.grid(column=8, row=22, columnspan=3)
WebsiteWindow.focus()

EMAIL=Label(text="     USERNAME", bg="black", fg="#545454")
EMAIL.grid(column=8, row=27, columnspan=1)
EmailWindow=Entry(width=24)
EmailWindow.grid(column=8, row=27, columnspan=3)
#EmailWindow.insert(0, "  ")

PASSWORD=Label(text="     PASSWORD",bg="black", fg="#545454")
PASSWORD.grid(column=8, row=28, columnspan=1)
PasswordWindow=Entry(width=24)
PasswordWindow.grid(column=8, row=28, columnspan=3)


EMPTY=Label(text="   ",bg="black", fg="grey")
EMPTY.grid(column=8, row=30, columnspan=1)

Save = Button(text="          Save password           ",  bg="grey", fg="black", command= save, width = 20)
Save.grid(column=8, row=31, columnspan=3)

Generate = Button(text="       Generate Password      ", bg="grey", command= generate, width = 20)
Generate.grid(column=8, row=32, columnspan=3)

Generate = Button(text="       FIND PASSWORD      ", bg="#E2521D", command= find, width = 20)
Generate.grid(column=8, row=33, columnspan=3)



#####################      EMPTY SPACE       ########################################

EMPTY=Label(text="   ",bg="black", fg="grey")
EMPTY.grid(column=8, row=34, columnspan=1)
EMPTY=Label(text=f"",bg="black", fg="grey")
EMPTY.grid(column=8, row=35, columnspan=1)
EMPTY=Label(text=f"",bg="black", fg="grey")
EMPTY.grid(column=8, row=36, columnspan=1)

#####################     COPYRIGHT LABEL   #########################################

mytitle=Label(text="Locksmith /// by v.ant ",bg="black", fg="#E2521D")
mytitle.grid(column=8, row=38, columnspan=3)






canvas.grid()
canvas.mainloop()