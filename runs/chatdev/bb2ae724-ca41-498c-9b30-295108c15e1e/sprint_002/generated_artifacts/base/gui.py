'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
def create_student():
    name = name_entry.get()
    response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
    if response.status_code == 200:
        result_label.config(text=f"Student created: {response.json()['name']}")
    else:
        result_label.config(text="Error creating student")
app = tk.Tk()
app.title("Student API")
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Button(app, text="Create Student", command=create_student).pack()
result_label = tk.Label(app, text="")
result_label.pack()
app.mainloop()