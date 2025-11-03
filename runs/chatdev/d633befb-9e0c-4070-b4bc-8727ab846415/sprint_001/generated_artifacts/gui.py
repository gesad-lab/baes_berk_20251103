'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students"
def add_student():
    name = name_entry.get()
    response = requests.post(API_URL, json={"name": name})
    if response.status_code == 200:
        result_label.config(text="Student added successfully!")
    else:
        result_label.config(text="Error adding student.")
# Create the main window
root = tk.Tk()
root.title("Student Management")
# Create and place the widgets
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
# Run the GUI
root.mainloop()