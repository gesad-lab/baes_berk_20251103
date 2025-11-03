'''
Simple GUI for interacting with the FastAPI backend.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students/"
def create_student():
    name = name_entry.get()
    email = email_entry.get()
    response = requests.post(API_URL, json={"name": name, "email": email})
    if response.status_code == 200:
        result_label.config(text="Student created successfully!")
    else:
        result_label.config(text=f"Error creating student: {response.json().get('detail', 'Unknown error')}")
def list_students():
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        students_list.delete(0, tk.END)
        for student in students:
            students_list.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}")
# Create the main window
root = tk.Tk()
root.title("Student Management")
# Create input fields
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Student Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()
# Create buttons
tk.Button(root, text="Create Student", command=create_student).pack()
tk.Button(root, text="List Students", command=list_students).pack()
# Create result label
result_label = tk.Label(root, text="")
result_label.pack()
# Create listbox for students
students_list = tk.Listbox(root)
students_list.pack()
# Start the GUI event loop
root.mainloop()