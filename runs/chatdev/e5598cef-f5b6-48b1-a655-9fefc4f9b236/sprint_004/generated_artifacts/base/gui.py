'''
Simple GUI for interacting with the FastAPI backend.
'''
import tkinter as tk
import requests
API_URL_STUDENT = "http://127.0.0.1:8000/students/"
API_URL_COURSE = "http://127.0.0.1:8000/courses/"
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
# Create the main window
root = tk.Tk()
root.title("Student and Course Management")
# Create input fields for students
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Student Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()
# Create buttons for students
tk.Button(root, text="Create Student", command=create_student).pack()
tk.Button(root, text="List Students", command=list_students).pack()
# Create result label for students
result_label = tk.Label(root, text="")
result_label.pack()
# Create listbox for students
students_list = tk.Listbox(root)
students_list.pack()
# Create input fields for courses
tk.Label(root, text="Course Name:").pack()
course_name_entry = tk.Entry(root)
course_name_entry.pack()
tk.Label(root, text="Course Level:").pack()
course_level_entry = tk.Entry(root)
course_level_entry.pack()
# Create buttons for courses
tk.Button(root, text="Create Course", command=create_course).pack()
tk.Button(root, text="List Courses", command=list_courses).pack()
# Create result label for courses
course_result_label = tk.Label(root, text="")
course_result_label.pack()
# Create listbox for courses
courses_list = tk.Listbox(root)
courses_list.pack()
# Start the GUI event loop
root.mainloop()