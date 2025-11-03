'''
Simple GUI using Tkinter to interact with the API for managing students, courses, and teachers.
'''
import tkinter as tk
import requests
API_URL_STUDENTS = "http://127.0.0.1:8000/students/"
API_URL_COURSES = "http://127.0.0.1:8000/courses/"
API_URL_TEACHERS = "http://127.0.0.1:8000/teachers/"
API_URL_ADD_COURSE = "http://127.0.0.1:8000/students/{student_id}/courses/{course_id}"
API_URL_GET_STUDENT_COURSES = "http://127.0.0.1:8000/students/{student_id}/courses"
def create_student():
    name = name_entry.get()
    email = email_entry.get()
    response = requests.post(API_URL_STUDENTS, json={"name": name, "email": email})
    if response.status_code == 200:
        result_label.config(text="Student created successfully!")
    else:
        result_label.config(text=f"Error creating student: {response.json().get('detail', 'Unknown error')}")
def get_students():
    response = requests.get(API_URL_STUDENTS)
    if response.status_code == 200:
        students = response.json()
        students_list.delete(0, tk.END)
        for student in students:
            students_list.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}")
    else:
        result_label.config(text="Error fetching students.")
def create_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    response = requests.post(API_URL_COURSES, json={"name": name, "level": level})
    if response.status_code == 200:
        course_result_label.config(text="Course created successfully!")
    else:
        course_result_label.config(text=f"Error creating course: {response.json().get('detail', 'Unknown error')}")
def get_courses():
    response = requests.get(API_URL_COURSES)
    if response.status_code == 200:
        courses = response.json()
        courses_list.delete(0, tk.END)
        for course in courses:
            courses_list.insert(tk.END, f"{course['id']}: {course['name']} - {course['level']}")
    else:
        course_result_label.config(text="Error fetching courses.")
def create_teacher():
    name = teacher_name_entry.get()
    email = teacher_email_entry.get()
    response = requests.post(API_URL_TEACHERS, json={"name": name, "email": email})
    if response.status_code == 200:
        teacher_result_label.config(text="Teacher created successfully!")
    else:
        teacher_result_label.config(text=f"Error creating teacher: {response.json().get('detail', 'Unknown error')}")
def get_teachers():
    response = requests.get(API_URL_TEACHERS)
    if response.status_code == 200:
        teachers = response.json()
        teachers_list.delete(0, tk.END)
        for teacher in teachers:
            teachers_list.insert(tk.END, f"{teacher['id']}: {teacher['name']} - {teacher['email']}")
    else:
        teacher_result_label.config(text="Error fetching teachers.")
app = tk.Tk()
app.title("Student, Course, and Teacher Management")
# Student Management
tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()
tk.Label(app, text="Student Email:").pack()
email_entry = tk.Entry(app)
email_entry.pack()
tk.Button(app, text="Create Student", command=create_student).pack()
tk.Button(app, text="Get Students", command=get_students).pack()
result_label = tk.Label(app, text="")
result_label.pack()
students_list = tk.Listbox(app)
students_list.pack()
# Course Management
tk.Label(app, text="Course Name:").pack()
course_name_entry = tk.Entry(app)
course_name_entry.pack()
tk.Label(app, text="Course Level:").pack()
course_level_entry = tk.Entry(app)
course_level_entry.pack()
tk.Button(app, text="Create Course", command=create_course).pack()
tk.Button(app, text="Get Courses", command=get_courses).pack()
course_result_label = tk.Label(app, text="")
course_result_label.pack()
courses_list = tk.Listbox(app)
courses_list.pack()
# Teacher Management
tk.Label(app, text="Teacher Name:").pack()
teacher_name_entry = tk.Entry(app)
teacher_name_entry.pack()
tk.Label(app, text="Teacher Email:").pack()
teacher_email_entry = tk.Entry(app)
teacher_email_entry.pack()
tk.Button(app, text="Create Teacher", command=create_teacher).pack()
tk.Button(app, text="Get Teachers", command=get_teachers).pack()
teacher_result_label = tk.Label(app, text="")
teacher_result_label.pack()
teachers_list = tk.Listbox(app)
teachers_list.pack()
app.mainloop()