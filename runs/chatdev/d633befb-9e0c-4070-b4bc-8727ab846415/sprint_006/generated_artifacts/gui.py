'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL_STUDENT = "http://127.0.0.1:8000/students"
API_URL_COURSE = "http://127.0.0.1:8000/courses"
API_URL_TEACHER = "http://127.0.0.1:8000/teachers"
API_URL_ENROLL = "http://127.0.0.1:8000/students/{}/courses/{}"
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
    teacher_id = teacher_id_entry.get()  # Get teacher ID from input
    response = requests.post(API_URL_COURSE, json={"name": name, "level": level, "teacher_id": teacher_id})
    if response.status_code == 200:
        course_result_label.config(text="Course added successfully!")
    else:
        course_result_label.config(text="Error adding course.")
def add_teacher():
    name = teacher_name_entry.get()
    email = teacher_email_entry.get()
    response = requests.post(API_URL_TEACHER, json={"name": name, "email": email})
    if response.status_code == 200:
        teacher_result_label.config(text="Teacher added successfully!")
    else:
        teacher_result_label.config(text="Error adding teacher.")
# Create the main window
root = tk.Tk()
root.title("Student, Course, and Teacher Management")
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
tk.Label(root, text="Teacher ID:").pack()  # New label for Teacher ID
teacher_id_entry = tk.Entry(root)  # New entry for Teacher ID
teacher_id_entry.pack()
add_course_button = tk.Button(root, text="Add Course", command=add_course)
add_course_button.pack()
course_result_label = tk.Label(root, text="")
course_result_label.pack()
# Teacher section
tk.Label(root, text="Teacher Name:").pack()
teacher_name_entry = tk.Entry(root)
teacher_name_entry.pack()
tk.Label(root, text="Teacher Email:").pack()
teacher_email_entry = tk.Entry(root)
teacher_email_entry.pack()
add_teacher_button = tk.Button(root, text="Add Teacher", command=add_teacher)
add_teacher_button.pack()
teacher_result_label = tk.Label(root, text="")
teacher_result_label.pack()
# Enrollment section
tk.Label(root, text="Student ID to Enroll:").pack()
student_id_entry = tk.Entry(root)
student_id_entry.pack()
tk.Label(root, text="Course ID to Enroll In:").pack()
course_id_entry = tk.Entry(root)
course_id_entry.pack()
# Run the GUI
root.mainloop()