# CodSoft-Internship (Python Programming) TASK: To make a "TO-DO-LIST"
from tkinter import *
from tkinter import messagebox
import os

#-------------------------------  functionality part -----------------------------------

# optional-- making a folder for tasks 
#if not os.path.exists("tasks"):
#    os.mkdir("tasks")

def add():
    TASK = task_entry.get()
    if TASK != "":
        #write code to open tasks folder to wrtte tasks in it from task_entry.get()
        #task_list.append(task_entry.get())
        l_box.insert(0, TASK)
        task_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "No Task Is Entered")

def delete():
    try:
        selected_task = l_box.curselection()[0]
        l_box.delete(selected_task)
        #write code to permanently delete the specified task from tasks folder as well
    except:
        messagebox.showerror("Error", "Please select a task to delete")

def delete_all():
    result = messagebox.askyesno("Confirm", "Do you want to delete all tasks?")
    if result:
        l_box.delete(0,END)
        tasks.delete(0, END)
        #write code to delete all the tasks permanently from tasks folder

#------------------------------------  GUI part ----------------------------------------
root = Tk()
root.geometry("1350x650+1+7")
root.title("TO-DO-LIST")
root.iconbitmap("list_icon.ico")
root.config(bg="turquoise3")


# main heading_label
heading_label = Label(root, text="TO-DO-LIST",font=("times new roman",40,"bold","italic"),
    bg="turquoise3",fg="black")
heading_label.pack(padx=10,pady=20)

''' task frame for options including task_entry field, add_task button,
    delete_task button, delete_all_task button and lastly author details frame. '''
task_frame = Frame(root,bd=5,relief=RIDGE,bg="turquoise3")
task_frame.pack(side=LEFT,fill=Y,padx=50)

enter_task_label = Label(task_frame,text="Enter The Task",font=("arial",16,"bold"),
    bg="turquoise3",fg="black")
enter_task_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")

task_entry = Entry(task_frame,font=("arial",18),bg="white",fg="black",width=40,
    bd=4,relief=GROOVE)
task_entry.grid(row=1,column=0,padx=10,pady=10)

# Add Task Button
add_task_button = Button(task_frame,text="Add Task", font=("arial black",14),
    bg="white",fg="black",width=40,command=add)
add_task_button.grid(row=2,column=0,padx=10,pady=10)

# Delete Task Button
delete_task_button = Button(task_frame,text="Delete Task", font=("arial black",14),
    bg="white",fg="black",width=40,command=delete)
delete_task_button.grid(row=3,column=0,padx=10,pady=10)

# Delete All Task Button
delete_all_task_button = Button(task_frame,text="Delete All Task", font=("arial black",14),
    bg="white",fg="black",width=40,command=delete_all)
delete_all_task_button.grid(row=4,column=0,padx=10,pady=10)


# making author details frame
author_details_frame = LabelFrame(task_frame,text="Author Details",
    font=("times new roman",20,"bold"),bg="turquoise3",fg="gray10",bd=5,relief=SOLID)
author_details_frame.grid(row=5,column=0,padx=5,pady=20)

author_name = Label(author_details_frame,text="\nMade By: \tMuhammad Omer Moazzam",
    font=("arial",12,"underline","bold"),bg="turquoise3",fg="black")
author_name.grid(row=0,column=0,sticky="w")

author_designation = Label(author_details_frame,text="\nDesignation:  \tUndergraduate, Software Engineering",
    font=("arial",12,"underline","bold"),bg="turquoise3",fg="black")
author_designation.grid(row=1,column=0,sticky="w")

author_institute = Label(author_details_frame,text="\nInstitute:  \tSir Syed University of Engineering and Technology\n",
    font=("arial",12,"underline","bold"),bg="turquoise3",fg="black")
author_institute.grid(row=2,column=0,sticky="w")


# display frame which includes Listbox for task_list 
display_frame = Frame(root,)
display_frame.pack(side=RIGHT,fill=Y,padx=50)

# making scroll bar for Listbox
scrollbar = Scrollbar(display_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

# making Listbox to display tasks
l_box = Listbox(display_frame,bd=5,relief=RIDGE, font=("arial",16),width=60,
    selectbackground="gray30",yscrollcommand=scrollbar.set)
l_box.pack(side=RIGHT,fill=Y)

# configuring the scrollbar with textarea
scrollbar.config(command=l_box.yview)

root.mainloop()