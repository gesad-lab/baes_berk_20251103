'''
Simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students/"
def create_student():
    name = name_entry.get()
    response = requests.post(API_URL, json={"name": name})
    if response.status_code == 200:
        result_label.config(text="Student created successfully!")
    else:
        result_label.config(text=f"Error creating student: {response.json().get('detail', 'Unknown error')}")
def get_students():
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        students_list.delete(0, tk.END)
        for student in students:
            students_list.insert(tk.END, f"{student['id']}: {student['name']}")
    else:
        result_label.config(text="Error fetching students.")
app = tk.Tk()
app.title("Student Management")
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Button(app, text="Create Student", command=create_student).pack()
tk.Button(app, text="Get Students", command=get_students).pack()
result_label = tk.Label(app, text="")
result_label.pack()
students_list = tk.Listbox(app)
students_list.pack()
app.mainloop()