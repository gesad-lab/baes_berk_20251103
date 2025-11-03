'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
def add_student():
    name = name_entry.get()
    email = email_entry.get()  # Get the email from the entry
    try:
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Include email in the request
        response.raise_for_status()  # Raise an error for bad responses
        result_label.config(text="Student added successfully!")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error adding student: {e}")
def get_students():
    try:
        response = requests.get("http://127.0.0.1:8000/students/")
        response.raise_for_status()  # Raise an error for bad responses
        students = response.json()
        students_list = "\n".join([f"{student['id']}: {student['name']} - {student['email']}" for student in students])  # Include email in the display
        result_label.config(text=students_list)
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error fetching students: {e}")
app = tk.Tk()
app.title("Student Management")
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Label(app, text="Student Email:").pack()  # Add label for email
email_entry = tk.Entry(app)  # Create entry for email
email_entry.pack()
tk.Button(app, text="Add Student", command=add_student).pack()
tk.Button(app, text="Get Students", command=get_students).pack()
result_label = tk.Label(app, text="")
result_label.pack()
app.mainloop()