'''
Simple GUI for interacting with the FastAPI application.
'''
import tkinter as tk
import requests
def create_student():
    name = name_entry.get()
    email = email_entry.get()
    course_ids = course_ids_entry.get().split(",")  # Get course IDs from entry
    response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email, "course_ids": course_ids})
    if response.status_code == 200:
        result_label.config(text=f"Student created: {response.json()['name']}")
    else:
        result_label.config(text="Error creating student")
def create_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
    if response.status_code == 200:
        result_label.config(text=f"Course created: {response.json()['name']}")
    else:
        result_label.config(text="Error creating course")
app = tk.Tk()
app.title("Student and Course Registration")
# Student Registration
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Label(app, text="Student Email:").pack()
email_entry = tk.Entry(app)
email_entry.pack()
tk.Label(app, text="Course IDs (comma-separated):").pack()  # New entry for course IDs
course_ids_entry = tk.Entry(app)
course_ids_entry.pack()
tk.Button(app, text="Create Student", command=create_student).pack()
# Course Registration
tk.Label(app, text="Course Name:").pack()
course_name_entry = tk.Entry(app)
course_name_entry.pack()
tk.Label(app, text="Course Level:").pack()
course_level_entry = tk.Entry(app)
course_level_entry.pack()
tk.Button(app, text="Create Course", command=create_course).pack()
result_label = tk.Label(app, text="")
result_label.pack()
app.mainloop()