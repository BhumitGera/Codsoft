from tkinter import *
import string
import random


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+numbers,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password = passwordField.get()
    root.clipboard_clear()
    root.clipboard_append(random_password)
    root.update()

def clear():
    passwordField.delete(0, END)

root=Tk()
root.title("Password Generator")
root.geometry("300x340+300+50")
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.place(x=30 , y=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.place(x=115 , y=50)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.place(x=115 , y=90)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.place(x=115 , y=130)

lengthLabel=Label(root,text='Password Length',font=Font,bg='gray20',fg='white')
lengthLabel.place(x=20 , y=170)
length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.place(x=200 , y=170)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.place(x=115 , y=210)

passwordField=Entry(root,width=23,bd=2,font=Font)
passwordField.place(x=45 , y=250)

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.place(x=65 , y=290)

clearButton = Button(root, text='Clear', font=Font, command=clear)
clearButton.place(x=180, y=290)

root.mainloop()

