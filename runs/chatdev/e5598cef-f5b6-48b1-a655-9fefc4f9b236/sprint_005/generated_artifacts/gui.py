'''
Simple GUI for interacting with the FastAPI backend.
'''
import tkinter as tk
import requests
API_URL_STUDENT = "http://127.0.0.1:8000/students/"
API_URL_COURSE = "http://127.0.0.1:8000/courses/"
API_URL_TEACHER = "http://127.0.0.1:8000/teachers/"
API_URL_ENROLL = "http://127.0.0.1:8000/students/{student_id}/courses/{course_id}"
def create_student():
    name = name_entry.get()
    email = email_entry.get()
    response = requests.post(API_URL_STUDENT, json={"name": name, "email": email})
    if response.status_code == 200:
        result_label.config(text="Student created successfully!")
    else:
        result_label.config(text=f"Error creating student: {response.json().get('detail', 'Unknown error')}")
def list_students():
    response = requests.get(API_URL_STUDENT)
    if response.status_code == 200:
        students = response.json()
        students_list.delete(0, tk.END)
        for student in students:
            students_list.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}")
def create_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    response = requests.post(API_URL_COURSE, json={"name": name, "level": level})
    if response.status_code == 200:
        course_result_label.config(text="Course created successfully!")
    else:
        course_result_label.config(text=f"Error creating course: {response.json().get('detail', 'Unknown error')}")
def list_courses():
    response = requests.get(API_URL_COURSE)
    if response.status_code == 200:
        courses = response.json()
        courses_list.delete(0, tk.END)
        for course in courses:
            courses_list.insert(tk.END, f"{course['id']}: {course['name']} - {course['level']}")
def create_teacher():
    name = teacher_name_entry.get()
    email = teacher_email_entry.get()
    response = requests.post(API_URL_TEACHER, json={"name": name, "email": email})
    if response.status_code == 200:
        teacher_result_label.config(text="Teacher created successfully!")
    else:
        teacher_result_label.config(text=f"Error creating teacher: {response.json().get('detail', 'Unknown error')}")
def list_teachers():
    response = requests.get(API_URL_TEACHER)
    if response.status_code == 200:
        teachers = response.json()
        teachers_list.delete(0, tk.END)
        for teacher in teachers:
            teachers_list.insert(tk.END, f"{teacher['id']}: {teacher['name']} - {teacher['email']}")
def enroll_student():
    student_id = student_id_entry.get()
    course_id = course_id_entry.get()
    response = requests.post(API_URL_ENROLL.format(student_id=student_id, course_id=course_id))
    if response.status_code == 200:
        enroll_result_label.config(text="Student enrolled in course successfully!")
    else:
        enroll_result_label.config(text=f"Error enrolling student: {response.json().get('detail', 'Unknown error')}")
# Create the main window
root = tk.Tk()
root.title("Student, Course, and Teacher Management")
# Create input fields for students
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Student Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()
tk.Button(root, text="Create Student", command=create_student).pack()
tk.Button(root, text="List Students", command=list_students).pack()
result_label = tk.Label(root, text="")
result_label.pack()
students_list = tk.Listbox(root)
students_list.pack()
# Create input fields for courses
tk.Label(root, text="Course Name:").pack()
course_name_entry = tk.Entry(root)
course_name_entry.pack()
tk.Label(root, text="Course Level:").pack()
course_level_entry = tk.Entry(root)
course_level_entry.pack()
tk.Button(root, text="Create Course", command=create_course).pack()
tk.Button(root, text="List Courses", command=list_courses).pack()
course_result_label = tk.Label(root, text="")
course_result_label.pack()
courses_list = tk.Listbox(root)
courses_list.pack()
# Create input fields for teachers
tk.Label(root, text="Teacher Name:").pack()
teacher_name_entry = tk.Entry(root)
teacher_name_entry.pack()
tk.Label(root, text="Teacher Email:").pack()
teacher_email_entry = tk.Entry(root)
teacher_email_entry.pack()
tk.Button(root, text="Create Teacher", command=create_teacher).pack()
tk.Button(root, text="List Teachers", command=list_teachers).pack()
teacher_result_label = tk.Label(root, text="")
teacher_result_label.pack()
teachers_list = tk.Listbox(root)
teachers_list.pack()
# Create input fields for enrollment
tk.Label(root, text="Student ID to Enroll:").pack()
student_id_entry = tk.Entry(root)
student_id_entry.pack()
tk.Label(root, text="Course ID to Enroll In:").pack()
course_id_entry = tk.Entry(root)
course_id_entry.pack()
tk.Button(root, text="Enroll Student in Course", command=enroll_student).pack()
enroll_result_label = tk.Label(root, text="")
enroll_result_label.pack()
# Start the GUI event loop
root.mainloop()