'''
Simple GUI for interacting with the FastAPI application.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students/"
def create_student():
    name = name_entry.get()
    email = email_entry.get()  # Get email from new entry
    if not name or not email:  # Check for empty name or email
        result_label.config(text="Name and email cannot be empty")
        return
    response = requests.post(API_URL, json={"name": name, "email": email})  # Include email in request
    if response.status_code == 200:
        result_label.config(text=f"Student created: {response.json()['name']}")
    else:
        result_label.config(text="Error creating student: " + response.json().get("detail", "Unknown error"))
def get_students():
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        result_label.config(text=f"Students: {', '.join([s['name'] for s in students])}")
    else:
        result_label.config(text="Error fetching students")
# Create the GUI window
window = tk.Tk()
window.title("Student API")
tk.Label(window, text="Student Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()
tk.Label(window, text="Student Email:").pack()  # Add label for email
email_entry = tk.Entry(window)  # Create entry for email
email_entry.pack()
tk.Button(window, text="Create Student", command=create_student).pack()
tk.Button(window, text="Get Students", command=get_students).pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()