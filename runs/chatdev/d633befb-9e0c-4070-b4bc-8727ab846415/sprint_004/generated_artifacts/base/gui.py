'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL_STUDENT = "http://127.0.0.1:8000/students"
API_URL_COURSE = "http://127.0.0.1:8000/courses"
def add_student():
    name = name_entry.get()
    email = email_entry.get()
    response = requests.post(API_URL_STUDENT, json={"name": name, "email": email})
    if response.status_code == 200:
        result_label.config(text="Student added successfully!")
    else:
        result_label.config(text="Error adding student.")
def add_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    response = requests.post(API_URL_COURSE, json={"name": name, "level": level})
    if response.status_code == 200:
        course_result_label.config(text="Course added successfully!")
    else:
        course_result_label.config(text="Error adding course.")
# Create the main window
root = tk.Tk()
root.title("Student and Course Management")
# Student section
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Student Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
# Course section
tk.Label(root, text="Course Name:").pack()
course_name_entry = tk.Entry(root)
course_name_entry.pack()
tk.Label(root, text="Course Level:").pack()
course_level_entry = tk.Entry(root)
course_level_entry.pack()
add_course_button = tk.Button(root, text="Add Course", command=add_course)
add_course_button.pack()
course_result_label = tk.Label(root, text="")
course_result_label.pack()
# Run the GUI
root.mainloop()