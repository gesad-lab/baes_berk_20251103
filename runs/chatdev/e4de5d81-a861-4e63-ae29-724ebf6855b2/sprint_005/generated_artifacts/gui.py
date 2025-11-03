'''
Simple GUI for interacting with the FastAPI backend using Tkinter.
'''
import tkinter as tk
import requests
API_URL_STUDENTS = "http://127.0.0.1:8000/students/"
API_URL_COURSES = "http://127.0.0.1:8000/courses/"
API_URL_TEACHERS = "http://127.0.0.1:8000/teachers/"
def create_student():
    name = name_entry.get()
    email = email_entry.get()
    course_ids = [int(course_id) for course_id in course_ids_entry.get().split(',') if course_id.isdigit()]
    response = requests.post(API_URL_STUDENTS, json={"name": name, "email": email, "course_ids": course_ids})
    if response.status_code == 200:
        result_label.config(text="Student created successfully!")
    else:
        result_label.config(text=f"Error creating student: {response.json().get('detail', 'Unknown error')}")
def create_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    response = requests.post(API_URL_COURSES, json={"name": name, "level": level})
    if response.status_code == 200:
        course_result_label.config(text="Course created successfully!")
    else:
        course_result_label.config(text=f"Error creating course: {response.json().get('detail', 'Unknown error')}")
def create_teacher():
    name = teacher_name_entry.get()
    email = teacher_email_entry.get()
    response = requests.post(API_URL_TEACHERS, json={"name": name, "email": email})
    if response.status_code == 200:
        teacher_result_label.config(text="Teacher created successfully!")
    else:
        teacher_result_label.config(text=f"Error creating teacher: {response.json().get('detail', 'Unknown error')}")
def get_students():
    response = requests.get(API_URL_STUDENTS)
    if response.status_code == 200:
        students = response.json()
        students_list.delete(0, tk.END)
        for student in students:
            students_list.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']} - Courses: {', '.join([str(course['id']) for course in student['courses']])}")
def get_courses():
    response = requests.get(API_URL_COURSES)
    if response.status_code == 200:
        courses = response.json()
        courses_list.delete(0, tk.END)
        for course in courses:
            courses_list.insert(tk.END, f"{course['id']}: {course['name']} - {course['level']}")
def get_teachers():
    response = requests.get(API_URL_TEACHERS)
    if response.status_code == 200:
        teachers = response.json()
        teachers_list.delete(0, tk.END)
        for teacher in teachers:
            teachers_list.insert(tk.END, f"{teacher['id']}: {teacher['name']} - {teacher['email']}")
# Create the main window
root = tk.Tk()
root.title("Student, Course, and Teacher Management")
# Create input field for student name
name_label = tk.Label(root, text="Student Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
# Create input field for student email
email_label = tk.Label(root, text="Student Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()
# Create input field for course IDs
course_ids_label = tk.Label(root, text="Course IDs (comma-separated):")
course_ids_label.pack()
course_ids_entry = tk.Entry(root)
course_ids_entry.pack()
# Create button to add student
add_button = tk.Button(root, text="Add Student", command=create_student)
add_button.pack()
# Create button to get students
get_button = tk.Button(root, text="Get Students", command=get_students)
get_button.pack()
# Create listbox to display students
students_list = tk.Listbox(root)
students_list.pack()
# Create label for result messages
result_label = tk.Label(root, text="")
result_label.pack()
# Create input field for course name
course_name_label = tk.Label(root, text="Course Name:")
course_name_label.pack()
course_name_entry = tk.Entry(root)
course_name_entry.pack()
# Create input field for course level
course_level_label = tk.Label(root, text="Course Level:")
course_level_label.pack()
course_level_entry = tk.Entry(root)
course_level_entry.pack()
# Create button to add course
add_course_button = tk.Button(root, text="Add Course", command=create_course)
add_course_button.pack()
# Create button to get courses
get_courses_button = tk.Button(root, text="Get Courses", command=get_courses)
get_courses_button.pack()
# Create listbox to display courses
courses_list = tk.Listbox(root)
courses_list.pack()
# Create label for course result messages
course_result_label = tk.Label(root, text="")
course_result_label.pack()
# Create input field for teacher name
teacher_name_label = tk.Label(root, text="Teacher Name:")
teacher_name_label.pack()
teacher_name_entry = tk.Entry(root)
teacher_name_entry.pack()
# Create input field for teacher email
teacher_email_label = tk.Label(root, text="Teacher Email:")
teacher_email_label.pack()
teacher_email_entry = tk.Entry(root)
teacher_email_entry.pack()
# Create button to add teacher
add_teacher_button = tk.Button(root, text="Add Teacher", command=create_teacher)
add_teacher_button.pack()
# Create button to get teachers
get_teachers_button = tk.Button(root, text="Get Teachers", command=get_teachers)
get_teachers_button.pack()
# Create listbox to display teachers
teachers_list = tk.Listbox(root)
teachers_list.pack()
# Create label for teacher result messages
teacher_result_label = tk.Label(root, text="")
teacher_result_label.pack()
# Run the GUI loop
root.mainloop()