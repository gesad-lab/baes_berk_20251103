'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
def add_student():
    name = name_entry.get()
    email = email_entry.get()  # Get the email from the entry
    try:
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Include email in the request
        response.raise_for_status()  # Raise an error for bad responses
        result_label.config(text="Student added successfully!")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error adding student: {e}")
def get_students():
    try:
        response = requests.get("http://127.0.0.1:8000/students/")
        response.raise_for_status()  # Raise an error for bad responses
        students = response.json()
        students_list = "\n".join([f"{student['id']}: {student['name']} - {student['email']}" for student in students])  # Include email in the display
        result_label.config(text=students_list)
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error fetching students: {e}")
def add_teacher():
    name = teacher_name_entry.get()
    email = teacher_email_entry.get()
    try:
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})  # Include email in the request
        response.raise_for_status()  # Raise an error for bad responses
        result_label.config(text="Teacher added successfully!")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error adding teacher: {e}")
def get_teachers():
    try:
        response = requests.get("http://127.0.0.1:8000/teachers/")
        response.raise_for_status()  # Raise an error for bad responses
        teachers = response.json()
        teachers_list = "\n".join([f"{teacher['id']}: {teacher['name']} - {teacher['email']}" for teacher in teachers])  # Include email in the display
        result_label.config(text=teachers_list)
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error fetching teachers: {e}")
app = tk.Tk()
app.title("Student, Teacher and Course Management")
# Student Section
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Label(app, text="Student Email:").pack()  # Add label for email
email_entry = tk.Entry(app)  # Create entry for email
email_entry.pack()
tk.Button(app, text="Add Student", command=add_student).pack()
tk.Button(app, text="Get Students", command=get_students).pack()
# Teacher Section
tk.Label(app, text="Teacher Name:").pack()
teacher_name_entry = tk.Entry(app)
teacher_name_entry.pack()
tk.Label(app, text="Teacher Email:").pack()
teacher_email_entry = tk.Entry(app)
teacher_email_entry.pack()
tk.Button(app, text="Add Teacher", command=add_teacher).pack()
tk.Button(app, text="Get Teachers", command=get_teachers).pack()
# Course Section
tk.Label(app, text="Course Name:").pack()
course_name_entry = tk.Entry(app)
course_name_entry.pack()
tk.Label(app, text="Course Level:").pack()
course_level_entry = tk.Entry(app)
course_level_entry.pack()
tk.Button(app, text="Add Course", command=add_course).pack()
tk.Button(app, text="Get Courses", command=get_courses).pack()
# Enrollment Section
tk.Label(app, text="Student ID to Enroll:").pack()
student_id_entry = tk.Entry(app)
student_id_entry.pack()
tk.Label(app, text="Course ID to Enroll In:").pack()
course_id_entry = tk.Entry(app)
course_id_entry.pack()
tk.Button(app, text="Enroll Student in Course", command=enroll_student_in_course).pack()
result_label = tk.Label(app, text="")
result_label.pack()
app.mainloop()