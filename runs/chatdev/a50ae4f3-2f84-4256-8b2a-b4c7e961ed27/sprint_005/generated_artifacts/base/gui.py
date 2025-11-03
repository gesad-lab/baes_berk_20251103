'''
Simple GUI using Tkinter to interact with the API for managing students and courses.
'''
import tkinter as tk
import requests
API_URL_STUDENTS = "http://127.0.0.1:8000/students/"
API_URL_COURSES = "http://127.0.0.1:8000/courses/"
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
def add_course_to_student():
    student_id = int(student_id_entry.get())
    course_id = int(course_id_entry.get())
    response = requests.post(API_URL_ADD_COURSE.format(student_id=student_id, course_id=course_id})
    if response.status_code == 200:
        add_course_result_label.config(text="Course added to student successfully!")
    else:
        add_course_result_label.config(text=f"Error adding course: {response.json().get('detail', 'Unknown error')}")
def get_student_courses():
    student_id = int(student_id_entry.get())
    response = requests.get(API_URL_GET_STUDENT_COURSES.format(student_id=student_id))
    if response.status_code == 200:
        courses = response.json()
        student_courses_list.delete(0, tk.END)
        for course in courses:
            student_courses_list.insert(tk.END, f"{course['id']}: {course['name']} - {course['level']}")
    else:
        add_course_result_label.config(text="Error fetching student's courses.")
app = tk.Tk()
app.title("Student and Course Management")
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
# Add Course to Student
tk.Label(app, text="Student ID to add course:").pack()
student_id_entry = tk.Entry(app)
student_id_entry.pack()
tk.Label(app, text="Course ID to add:").pack()
course_id_entry = tk.Entry(app)
course_id_entry.pack()
tk.Button(app, text="Add Course to Student", command=add_course_to_student).pack()
add_course_result_label = tk.Label(app, text="")
add_course_result_label.pack()
# Get Student Courses
tk.Button(app, text="Get Student Courses", command=get_student_courses).pack()
student_courses_list = tk.Listbox(app)
student_courses_list.pack()
app.mainloop()