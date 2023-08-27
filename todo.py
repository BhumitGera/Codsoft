from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class todo:
    def __init__(self,root):
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('600x350+300+150')

        self.label = Label(self.root, text= 'To Do List App',
             font='Arial, 20 bold', width=10, bd=5, bg="red", fg='black')
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root, text= 'Add Task',
             font='Arial, 15 bold', width=10, bd=5, bg="red", fg='black')
        self.label2.place(x=450, y=55)

        self.label3 = Label(self.root, text= 'Tasks',
             font='Arial, 15 bold', width=10, bd=5, bg="red", fg='black')
        self.label3.place(x=150, y=55)

        self.main_text = Listbox(self.root, height=9, bd=5, width=30, font='Arial, 15 bold')
        self.main_text.place(x=50, y=100)

        self.text = Text(self.root, height=2, bd=5, width=23, font='Arial, 10 bold')
        self.text.place(x=420, y=120)

    
        
        
        def add():
            task = self.text.get(1.0, END).strip()
            if task:
                if "Edit Mode" in self.button.cget("text"):  
                    index = self.main_text.curselection()
                    if index:
                        self.main_text.delete(index)
                        self.main_text.insert(index, task)
                        self.button.config(text="Add")
                    else:
                       messagebox.showerror("Error", "No task selected for editing")
                else:
                    self.main_text.insert(END, task)
                with open('data.txt', 'a') as file:
                    file.write(task + '\n')
                self.text.delete(1.0, END)
            else:
                messagebox.showerror("Error", "Invalid task entry")
        

        def delete():
            dele = self.main_text.curselection()
            look = self.main_text.get(dele)
            with open('data.txt', 'r+') as f:
                new = f.readlines()
                f.seek(0)
                for line in new:
                    item = str(look)
                    if item not in line:
                       f.write(line)
                f.truncate()
            self.main_text.delete(dele)

        with open('data.txt', 'r') as file:
            read= file.readlines()
            for i in read:
                done = i.split()
                self.main_text.insert(END, done)
            file.close()
        
        def edit():
            selected_task = self.main_text.get(self.main_text.curselection())
            self.text.delete(1.0, END)
            self.text.insert(END, selected_task)

        for i in read:
            done = i.strip() 
            self.main_text.insert(END, done)

        

        self.button = Button(self.root, text= 'Add', font='arial, 18 bold italic',
                              width=7,bd=5, bg= 'red', fg = 'black', command=add) 
        self.button.place(x = 440, y = 165) 
        self.button2 = Button(self.root, text="Update", font="arial 18 bold",
                         width=7,bd=5, bg="red", fg="black", command=edit)
        self.button2.place(x=440, y=225)

        self.button3 = Button(self.root, text= 'Delete', font='arial, 18 bold italic',
                              width=7,bd=5, bg='red', fg ='black', command=delete) 
        self.button3.place(x = 440, y = 285)  



def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
