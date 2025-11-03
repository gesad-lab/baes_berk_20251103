'''
Implements a simple GUI using Tkinter to interact with the API for both Students and Teachers.
'''
import tkinter as tk
import requests
API_URL_STUDENT = "http://127.0.0.1:8000/students"
API_URL_TEACHER = "http://127.0.0.1:8000/teachers"
API_URL_COURSE = "http://127.0.0.1:8000/courses"
def submit_student():
    name = name_entry.get()
    email = email_entry.get()
    courses = courses_entry.get().split(",")
    response = requests.post(API_URL_STUDENT, json={"name": name, "email": email, "courses": courses})
    if response.status_code == 200:
        result_label.config(text=f"Student added: {response.json()['name']}")
    else:
        result_label.config(text="Error adding student")
def submit_teacher():
    name = teacher_name_entry.get()
    email = teacher_email_entry.get()
    response = requests.post(API_URL_TEACHER, json={"name": name, "email": email})
    if response.status_code == 200:
        teacher_result_label.config(text=f"Teacher added: {response.json()['name']}")
    else:
        teacher_result_label.config(text="Error adding teacher")
def submit_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    teacher_id = teacher_id_entry.get()
    response = requests.post(API_URL_COURSE, json={"name": name, "level": level, "teacher_id": teacher_id})
    if response.status_code == 200:
        course_result_label.config(text=f"Course added: {response.json()['name']}")
    else:
        course_result_label.config(text="Error adding course")
# Create the main window
root = tk.Tk()
root.title("Registration Dashboard")
# Student Registration
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Student Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()
tk.Label(root, text="Courses (comma-separated):").pack()
courses_entry = tk.Entry(root)
courses_entry.pack()
submit_button = tk.Button(root, text="Submit Student", command=submit_student)
submit_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
# Teacher Registration
tk.Label(root, text="Teacher Name:").pack()
teacher_name_entry = tk.Entry(root)
teacher_name_entry.pack()
tk.Label(root, text="Teacher Email:").pack()
teacher_email_entry = tk.Entry(root)
teacher_email_entry.pack()
submit_teacher_button = tk.Button(root, text="Submit Teacher", command=submit_teacher)
submit_teacher_button.pack()
teacher_result_label = tk.Label(root, text="")
teacher_result_label.pack()
# Course Registration
tk.Label(root, text="Course Name:").pack()
course_name_entry = tk.Entry(root)
course_name_entry.pack()
tk.Label(root, text="Course Level:").pack()
course_level_entry = tk.Entry(root)
course_level_entry.pack()
tk.Label(root, text="Teacher ID:").pack()
teacher_id_entry = tk.Entry(root)
teacher_id_entry.pack()
submit_course_button = tk.Button(root, text="Submit Course", command=submit_course)
submit_course_button.pack()
course_result_label = tk.Label(root, text="")
course_result_label.pack()
# Run the GUI loop
root.mainloop()