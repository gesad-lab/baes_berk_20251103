'''
Implements a simple GUI using Tkinter to interact with the API for managing students and courses.
'''
import tkinter as tk
import requests
API_URL_STUDENTS = "http://127.0.0.1:8000/students/"
API_URL_COURSES = "http://127.0.0.1:8000/courses/"
API_URL_ENROLL = "http://127.0.0.1:8000/enroll/"
def add_student():
    name = entry_name.get()
    email = entry_email.get()
    response = requests.post(API_URL_STUDENTS, json={"name": name, "email": email})
    if response.status_code == 200:
        label_response.config(text="Student added successfully!")
    else:
        label_response.config(text="Error adding student.")
def get_students():
    response = requests.get(API_URL_STUDENTS)
    if response.status_code == 200:
        students = response.json()
        label_response.config(text="Students: " + ", ".join([f"{s['name']} ({s['email']})" for s in students]))
    else:
        label_response.config(text="Error fetching students.")
def add_course():
    name = entry_course_name.get()
    level = entry_course_level.get()
    response = requests.post(API_URL_COURSES, json={"name": name, "level": level})
    if response.status_code == 200:
        label_course_response.config(text="Course added successfully!")
    else:
        label_course_response.config(text="Error adding course.")
def get_courses():
    response = requests.get(API_URL_COURSES)
    if response.status_code == 200:
        courses = response.json()
        label_course_response.config(text="Courses: " + ", ".join([f"{c['name']} ({c['level']})" for c in courses]))
    else:
        label_course_response.config(text="Error fetching courses.")
def enroll_student():
    student_id = entry_student_id.get()
    course_id = entry_course_id.get()
    response = requests.post(API_URL_ENROLL, json={"student_id": student_id, "course_id": course_id})
    if response.status_code == 200:
        label_enroll_response.config(text="Student enrolled in course successfully!")
    else:
        label_enroll_response.config(text="Error enrolling student.")
# Create the main window
root = tk.Tk()
root.title("Student and Course Management")
# Student section
label_name = tk.Label(root, text="Student Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()
label_email = tk.Label(root, text="Student Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()
button_add_student = tk.Button(root, text="Add Student", command=add_student)
button_add_student.pack()
button_get_students = tk.Button(root, text="Get Students", command=get_students)
button_get_students.pack()
label_response = tk.Label(root, text="")
label_response.pack()
# Course section
label_course_name = tk.Label(root, text="Course Name:")
label_course_name.pack()
entry_course_name = tk.Entry(root)
entry_course_name.pack()
label_course_level = tk.Label(root, text="Course Level:")
label_course_level.pack()
entry_course_level = tk.Entry(root)
entry_course_level.pack()
button_add_course = tk.Button(root, text="Add Course", command=add_course)
button_add_course.pack()
button_get_courses = tk.Button(root, text="Get Courses", command=get_courses)
button_get_courses.pack()
label_course_response = tk.Label(root, text="")
label_course_response.pack()
# Enrollment section
label_student_id = tk.Label(root, text="Student ID:")
label_student_id.pack()
entry_student_id = tk.Entry(root)
entry_student_id.pack()
label_course_id = tk.Label(root, text="Course ID:")
label_course_id.pack()
entry_course_id = tk.Entry(root)
entry_course_id.pack()
button_enroll_student = tk.Button(root, text="Enroll Student in Course", command=enroll_student)
button_enroll_student.pack()
label_enroll_response = tk.Label(root, text="")
label_enroll_response.pack()
# Start the GUI event loop
root.mainloop()