'''
Simple GUI for interacting with the FastAPI application.
'''
import tkinter as tk
import requests
API_URL_STUDENTS = "http://127.0.0.1:8000/students/"
API_URL_COURSES = "http://127.0.0.1:8000/courses/"
def create_student():
    name = name_entry.get()
    email = email_entry.get()  # Get email from new entry
    if not name or not email:  # Check for empty name or email
        result_label.config(text="Name and email cannot be empty")
        return
    response = requests.post(API_URL_STUDENTS, json={"name": name, "email": email})  # Include email in request
    if response.status_code == 200:
        result_label.config(text=f"Student created: {response.json()['name']}")
    else:
        result_label.config(text="Error creating student: " + response.json().get("detail", "Unknown error"))
def get_students():
    response = requests.get(API_URL_STUDENTS)
    if response.status_code == 200:
        students = response.json()
        result_label.config(text=f"Students: {', '.join([s['name'] for s in students])}")
    else:
        result_label.config(text="Error fetching students")
def create_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    if not name or not level:
        course_result_label.config(text="Name and level cannot be empty")
        return
    response = requests.post(API_URL_COURSES, json={"name": name, "level": level})
    if response.status_code == 200:
        course_result_label.config(text=f"Course created: {response.json()['name']}")
    else:
        course_result_label.config(text="Error creating course: " + response.json().get("detail", "Unknown error"))
def get_courses():
    response = requests.get(API_URL_COURSES)
    if response.status_code == 200:
        courses = response.json()
        course_result_label.config(text=f"Courses: {', '.join([c['name'] for c in courses])}")
    else:
        course_result_label.config(text="Error fetching courses")
# Create the GUI window
window = tk.Tk()
window.title("Student and Course API")
# Student section
tk.Label(window, text="Student Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()
tk.Label(window, text="Student Email:").pack()
email_entry = tk.Entry(window)
email_entry.pack()
tk.Button(window, text="Create Student", command=create_student).pack()
tk.Button(window, text="Get Students", command=get_students).pack()
result_label = tk.Label(window, text="")
result_label.pack()
# Course section
tk.Label(window, text="Course Name:").pack()
course_name_entry = tk.Entry(window)
course_name_entry.pack()
tk.Label(window, text="Course Level:").pack()
course_level_entry = tk.Entry(window)
course_level_entry.pack()
tk.Button(window, text="Create Course", command=create_course).pack()
tk.Button(window, text="Get Courses", command=get_courses).pack()
course_result_label = tk.Label(window, text="")
course_result_label.pack()
window.mainloop()