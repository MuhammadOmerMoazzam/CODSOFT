# By: MUHAMMAD OMER MOAZZAM
# CodSoft-Internship (Python Programming) TASK: To make a "CALCULATOR"
from tkinter import *

'''
# By simple method (i.e without GUI)
print("\t\t \"CALCULATOR\" ") 
# Making functions for arithmetic operations
def add(no1,no2):
    answer = no1 + no2
    return answer
def sub(no1,no2):
    answer = no1 - no2
    return answer
def mul(no1,no2):
    answer = no1 * no2
    return answer
def div(no1,no2):
    answer = no1 / no2
    return answer
def floor_div(no1,no2):
    answer = no1 // no2
    return answer
def exp(no1,no2):
    answer = no1 ** no2
    return answer
def mod(no1,no2):
    answer = no1 % no2
    return answer

# Making sentinel loop
CHOICE = "y"
while (CHOICE == 'y') or (CHOICE == 'Y') or (CHOICE == 'yes') or (CHOICE == 'YES') :
    # Making a menu for operators
    print("\n\t Menu to Choose Operation")
    print("Press \'1\' for \"Addition\" ")
    print("Press \'2\' for \"Subtraction\" ")
    print("Press \'3\' for \"Multiplication\" ")
    print("Press \'4\' for \"Division\" ")
    print("Press \'5\' for \"Floor Division\" ")
    print("Press \'6\' for \"Exponent\" ")
    print("Press \'7\' for \"Modulus\" \n")

    # Making input for user to enter numbers
    choice = eval(input("Enter choice from menu:\n "))
    number1 = eval(input("Enter first number:\n "))
    number2 = eval(input("Enter second number:\n "))

    # Making decision based on choice from menu
    if (choice == 1):
        result = add(number1,number2)
        print(f"{number1} + {number2} = {result}" ) # display result
    elif (choice == 2):
        result = sub(number1,number2)
        print(f"{number1} - {number2} = {result}" ) # display result
    elif (choice == 3):
        result = mul(number1,number2)
        print(f"{number1} * {number2} = {result}" ) # display result
    elif (choice == 4):
        result = div(number1,number2)
        print(f"{number1} / {number2} = {result}" ) # display result
    elif (choice == 5):
        result = floor_div(number1,number2)
        print(f"{number1} // {number2} = {result}" ) # display result
    elif (choice == 6):
        result = exp(number1,number2)
        print(f"{number1} ^ {number2} = {result}" ) # display result
    elif (choice == 7):
        result = mod(number1,number2)
        print(f"{number1} % {number2} = {result}" ) # display result
    else:
        print("Invalid Choice! choose a number between 1 to 7.")
    
    CHOICE = input("\nPress y|Y|yes|YES to do more calculation:")
'''

#-------------------------  functionality part  --------------------------------
def clear():
    display_entry.delete(0,END)

def click_buttons(event):
    text = event.widget.cget("text")
    display_entry.insert(END,text)

def equal():
    result = str(eval(display_entry.get()))
    display_entry.delete(0, END)
    display_entry.insert(END, result)

#--------------------- GUI using Tkinter starts here ---------------------------
root = Tk()
root.geometry("340x470")
root.resizable(False,False)
root.title("CALCULATOR")
root.iconbitmap("calculator_icon.ico")
root.config(bg="black")

# making display screen
display_entry = Entry(root,bd=10,relief=GROOVE,font=("Johannes Krenner",30),justify=RIGHT)
display_entry.pack(fill=X,side=TOP)

# making frame for buttons
buttons_frame = Frame(root,bg="black")
buttons_frame.pack(fill=X)

# all_clear button
clear_button = Button(buttons_frame,text="AC",font=("Johannes Krenner",20,"bold"),
bg="purple",fg="white",bd=2,relief=FLAT,width=8,command=clear)
clear_button.grid(row=0,column=0,padx=5,pady=10,columnspan=2)

# modulus button
mod_button = Button(buttons_frame,text="%",font=("Johannes Krenner",20,"bold"),
bg="gray40",fg="white",bd=4,relief=FLAT,width=3)
mod_button.grid(row=0,column=2,padx=5,pady=10)
mod_button.bind("<Button-1>", click_buttons)

# division button
division_button = Button(buttons_frame,text="/",font=("Johannes Krenner",20,"bold"),
bg="gray40",fg="white",bd=4,relief=FLAT,width=3)
division_button.grid(row=0,column=3,padx=5,pady=10)
division_button.bind("<Button-1>", click_buttons)

# multiplication button
mul_button = Button(buttons_frame,text="*",font=("Johannes Krenner",20,"bold"),
bg="gray40",fg="white",bd=4,relief=FLAT,width=3)
mul_button.grid(row=1,column=3,padx=5,pady=10)
mul_button.bind("<Button-1>", click_buttons)

# minus button
minus_button = Button(buttons_frame,text="-",font=("Johannes Krenner",20,"bold"),
bg="gray40",fg="white",bd=4,relief=FLAT,width=3)
minus_button.grid(row=2,column=3,padx=10,pady=10)
minus_button.bind("<Button-1>", click_buttons)

# plus button
plus_button = Button(buttons_frame,text="+",font=("Johannes Krenner",20,"bold"),
bg="gray40",fg="white",bd=4,relief=FLAT,width=3)
plus_button.grid(row=3,column=3,padx=10,pady=10)
plus_button.bind("<Button-1>", click_buttons)

# equal_to button
equal_to_button = Button(buttons_frame,text="=",font=("Johannes Krenner",20,"bold"),
bg="blue",fg="white",bd=4,relief=FLAT,width=8,command=equal)
equal_to_button.grid(row=4,column=2,padx=10,pady=10,columnspan=2)

# making 7 digit button
digit7_button = Button(buttons_frame,text="7",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit7_button.grid(row=1,column=0,padx=10,pady=10)
digit7_button.bind("<Button-1>", click_buttons)

# making 8 digit button
digit8_button = Button(buttons_frame,text="8",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit8_button.grid(row=1,column=1,padx=10,pady=10)
digit8_button.bind("<Button-1>", click_buttons)

# making 9 digit button
digit9_button = Button(buttons_frame,text="9",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit9_button.grid(row=1,column=2,padx=10,pady=10)
digit9_button.bind("<Button-1>", click_buttons)

# making 4 digit button
digit4_button = Button(buttons_frame,text="4",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit4_button.grid(row=2,column=0,padx=10,pady=10)
digit4_button.bind("<Button-1>", click_buttons)

# making 5 digit button
digit5_button = Button(buttons_frame,text="5",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit5_button.grid(row=2,column=1,padx=10,pady=10)
digit5_button.bind("<Button-1>", click_buttons)

# making 6 digit button
digit6_button = Button(buttons_frame,text="6",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit6_button.grid(row=2,column=2,padx=10,pady=10)
digit6_button.bind("<Button-1>", click_buttons)

# making 1 digit button
digit1_button = Button(buttons_frame,text="1",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit1_button.grid(row=3,column=0,padx=10,pady=10)
digit1_button.bind("<Button-1>", click_buttons)

# making 2 digit button
digit2_button = Button(buttons_frame,text="2",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit2_button.grid(row=3,column=1,padx=10,pady=10)
digit2_button.bind("<Button-1>", click_buttons)

# making 3 digit button
digit3_button = Button(buttons_frame,text="3",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit3_button.grid(row=3,column=2,padx=10,pady=10)
digit3_button.bind("<Button-1>", click_buttons)

# making 0 digit button
digit0_button = Button(buttons_frame,text="0",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
digit0_button.grid(row=4,column=1,padx=10,pady=10)
digit0_button.bind("<Button-1>", click_buttons)

# making decimal button
decimal_button = Button(buttons_frame,text=".",font=("Johannes Krenner",20,"bold"),
bg="gray20",fg="white",bd=4,relief=FLAT,width=3)
decimal_button.grid(row=4,column=0,padx=10,pady=10)
decimal_button.bind("<Button-1>", click_buttons)

root.mainloop()