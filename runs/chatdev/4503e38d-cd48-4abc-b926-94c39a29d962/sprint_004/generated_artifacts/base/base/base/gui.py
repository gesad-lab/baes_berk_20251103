'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students"
def submit_student():
    name = name_entry.get()
    response = requests.post(API_URL, json={"name": name})
    if response.status_code == 200:
        result_label.config(text=f"Student added: {response.json()['name']}")
    else:
        result_label.config(text="Error adding student")
# Create the main window
root = tk.Tk()
root.title("Student Registration")
# Create and place the widgets
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
submit_button = tk.Button(root, text="Submit", command=submit_student)
submit_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
# Run the GUI loop
root.mainloop()