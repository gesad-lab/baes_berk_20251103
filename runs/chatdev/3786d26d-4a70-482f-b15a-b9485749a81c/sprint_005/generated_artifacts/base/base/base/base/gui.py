'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students/"
def add_student():
    name = entry_name.get()
    response = requests.post(API_URL, json={"name": name})
    if response.status_code == 200:
        label_response.config(text="Student added successfully!")
    else:
        label_response.config(text="Error adding student.")
def get_students():
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        label_response.config(text="Students: " + ", ".join([s['name'] for s in students]))
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
button_add = tk.Button(root, text="Add Student", command=add_student)
button_add.pack()
button_get = tk.Button(root, text="Get Students", command=get_students)
button_get.pack()
label_response = tk.Label(root, text="")
label_response.pack()
# Start the GUI event loop
root.mainloop()