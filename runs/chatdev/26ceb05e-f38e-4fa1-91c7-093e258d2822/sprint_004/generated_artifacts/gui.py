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
def add_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    try:
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        response.raise_for_status()  # Raise an error for bad responses
        result_label.config(text="Course added successfully!")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error adding course: {e}")
def get_courses():
    try:
        response = requests.get("http://127.0.0.1:8000/courses/")
        response.raise_for_status()  # Raise an error for bad responses
        courses = response.json()
        courses_list = "\n".join([f"{course['id']}: {course['name']} - {course['level']}" for course in courses])
        result_label.config(text=courses_list)
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error fetching courses: {e}")
def enroll_student_in_course():
    student_id = student_id_entry.get()
    course_id = course_id_entry.get()
    try:
        response = requests.post(f"http://127.0.0.1:8000/enroll/", json={"student_id": student_id, "course_id": course_id})
        response.raise_for_status()  # Raise an error for bad responses
        result_label.config(text="Student enrolled in course successfully!")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error enrolling student: {e}")
app = tk.Tk()
app.title("Student and Course Management")
# Student Section
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Label(app, text="Student Email:").pack()  # Add label for email
email_entry = tk.Entry(app)  # Create entry for email
email_entry.pack()
tk.Button(app, text="Add Student", command=add_student).pack()
tk.Button(app, text="Get Students", command=get_students).pack()
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