# By: MUHAMMAD OMER MOAZZAM
# CodSoft-Internship (Python Programming) TASK: To make a "PASSWORD GENERATOR"
from tkinter import *
import random

#-------------------------------  functionality part -----------------------------------

# making a list containing multiple characters
random_chr = [
    "q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x",
    "c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H",
    "J","K","L","Z","X","C","V","B","N","M","1","2","3","4","5","6","7","8","9","0","!",
    "@","#","$","%","^","&","*" 
    ] 

def generate():
    noe = int(password_length_entry.get())
    display_password.delete(0, END)    
    for i in range(noe):
        PASSWORD = random.choice(random_chr)
        display_password.insert(END, PASSWORD)

def copy():
    copied_text = display_password.get()
    '''In Python's Tkinter library, you can use the "clipboard" module
    to interact with the system clipboard.'''
    
    # clearing any previous clipboard contents unsing clipboard_clear()
    root.clipboard_clear()

    # appending the copied_text into the clipboard 
    root.clipboard_append(copied_text)

    # updating the clipboard
    root.update()

#------------------------------------  GUI part ----------------------------------------

root = Tk()
root.geometry("580x550+450+100")
root.resizable(False,False)
root.title("PASSWORD GENERATOR")
root.iconbitmap("password_icon.ico")
root.config(bg="turquoise3")

# entry field to display password
display_password= Entry(root,font=("arial",30,"bold"),bd=10,relief=GROOVE)
display_password.pack(fill=X,padx=10,pady=5)

# frame for label and user entry
frame = Frame(root,bg="turquoise3")
frame.pack(fill=X)

label = Label(frame,text="Specify the Length of the Password:",
    font=("times new roman",22,"underline","bold"),bg="turquoise3")
label.pack(side=LEFT,anchor='nw',padx=10)

# making an Entry where user can specify the length of the password
password_length_entry = Entry(frame,font=("arial",22,"bold"),bd=5,relief=GROOVE,width=5)
password_length_entry.pack(fill=X,side=LEFT,anchor="nw",padx=10)
password_length_entry.insert(0, 0)

# buttons frame 
button_frame = Frame(root,bg="turquoise3")
button_frame.pack()

# button to generate password
generate_button = Button(button_frame,text="Generate Password",font=("times new roman",22,"bold"),
    width=20,command=generate)
generate_button.grid(row=0,column=0,padx=10,pady=20)

# button to copy password
copy_button = Button(button_frame,text="Copy Password",font=("times new roman",22,"bold"),
    width=20,command=copy)
copy_button.grid(row=1,column=0,padx=10,pady=10)

# making author details frame
author_details_frame = LabelFrame(root,text="Author Details",
    font=("times new roman",16,"bold"),bg="turquoise3",fg="gray10",bd=5,relief=SOLID)
author_details_frame.pack(padx=5,pady=20)

author_name = Label(author_details_frame,text="\nMade By: \tMuhammad Omer Moazzam",
    font=("arial",12,"underline","bold"),bg="turquoise3",fg="black")
author_name.grid(row=0,column=0,sticky="w")

author_designation = Label(author_details_frame,text="\nDesignation:  \tSoftware Engineering Student",
    font=("arial",12,"underline","bold"),bg="turquoise3",fg="black")
author_designation.grid(row=1,column=0,sticky="w")

author_institute = Label(author_details_frame,text="\nInstitute:  \tSir Syed University of Engineering and Technology\n",
    font=("arial",12,"underline","bold"),bg="turquoise3",fg="black")
author_institute.grid(row=2,column=0,sticky="w")

root.mainloop()