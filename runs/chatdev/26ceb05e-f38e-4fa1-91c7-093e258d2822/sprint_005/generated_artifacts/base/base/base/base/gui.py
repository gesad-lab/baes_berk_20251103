'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
def add_student():
    name = name_entry.get()
    try:
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        response.raise_for_status()  # Raise an error for bad responses
        result_label.config(text="Student added successfully!")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error adding student: {e}")
def get_students():
    try:
        response = requests.get("http://127.0.0.1:8000/students/")
        response.raise_for_status()  # Raise an error for bad responses
        students = response.json()
        students_list = "\n".join([f"{student['id']}: {student['name']}" for student in students])
        result_label.config(text=students_list)
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error fetching students: {e}")
app = tk.Tk()
app.title("Student Management")
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Button(app, text="Add Student", command=add_student).pack()
tk.Button(app, text="Get Students", command=get_students).pack()
result_label = tk.Label(app, text="")
result_label.pack()
app.mainloop()