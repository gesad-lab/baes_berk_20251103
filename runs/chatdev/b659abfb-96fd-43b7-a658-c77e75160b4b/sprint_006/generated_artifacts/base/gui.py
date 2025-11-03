'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students"
def add_student():
    name = name_entry.get()
    email = email_entry.get()
    course_ids = course_ids_entry.get().split(",")  # Get course IDs from input
    response = requests.post(API_URL, json={"name": name, "email": email, "course_ids": [int(id) for id in course_ids]})
    if response.status_code == 201:
        result_label.config(text="Student added successfully!")
    else:
        result_label.config(text="Failed to add student.")
# Create the main window
root = tk.Tk()
root.title("Student Management")
# Create and place the widgets
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Student Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()
tk.Label(root, text="Course IDs (comma-separated):").pack()
course_ids_entry = tk.Entry(root)
course_ids_entry.pack()
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
# Start the GUI event loop
root.mainloop()