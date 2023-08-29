import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name.strip() == "":
        messagebox.showerror("Error", "Name cannot be empty!")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    clear_entries()
    update_contact_list()

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, name)

def view_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        contact_details = contacts[selected_contact]
        messagebox.showinfo(
            "Contact Details",
            f"Name: {selected_contact}\nPhone: {contact_details['Phone']}\nEmail: {contact_details['Email']}\nAddress: {contact_details['Address']}"
        )

def search_contact():
    search_term = search_entry.get().strip()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term.lower() in details["Phone"]:
            contact_list.insert(tk.END, name)

def update_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name.strip() == "":
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        contacts[selected_contact] = {"Phone": phone, "Email": email, "Address": address}
        clear_entries()
        update_contact_list()

def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        del contacts[selected_contact]
        clear_entries()
        update_contact_list()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("300x500+300+50")
root.config(bg='gray')

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

contact_list = tk.Listbox(root)
contact_list.pack()

update_contact_list()
root.mainloop()
