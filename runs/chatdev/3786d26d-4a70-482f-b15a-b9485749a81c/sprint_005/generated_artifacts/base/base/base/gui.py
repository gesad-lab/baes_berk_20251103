'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students/"
def add_student():
    name = entry_name.get()
    email = entry_email.get()  # Get email from entry
    response = requests.post(API_URL, json={"name": name, "email": email})  # Include email in request
    if response.status_code == 200:
        label_response.config(text="Student added successfully!")
    else:
        label_response.config(text="Error adding student.")
def get_students():
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        label_response.config(text="Students: " + ", ".join([f"{s['name']} ({s['email']})" for s in students]))  # Show email
    else:
        label_response.config(text="Error fetching students.")
# Create the main window
root = tk.Tk()
root.title("Student Management")
# Create and place the widgets
label_name = tk.Label(root, text="Student Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()
label_email = tk.Label(root, text="Student Email:")  # New label for email
label_email.pack()
entry_email = tk.Entry(root)  # New entry for email
entry_email.pack()
button_add = tk.Button(root, text="Add Student", command=add_student)
button_add.pack()
button_get = tk.Button(root, text="Get Students", command=get_students)
button_get.pack()
label_response = tk.Label(root, text="")
label_response.pack()
# Start the GUI event loop
root.mainloop()