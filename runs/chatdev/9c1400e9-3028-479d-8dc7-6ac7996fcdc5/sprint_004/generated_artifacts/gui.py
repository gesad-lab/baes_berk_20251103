'''
Implements a simple GUI using Tkinter to interact with the API.
'''
import tkinter as tk
import requests
API_URL_STUDENT = "http://127.0.0.1:8000/students"
API_URL_COURSE = "http://127.0.0.1:8000/courses"
def submit_student():
    name = name_entry.get()
    email = email_entry.get()  # Added email entry
    response = requests.post(API_URL_STUDENT, json={"name": name, "email": email})  # Added email to request
    if response.status_code == 201:  # Changed to 201 for created resource
        result_label.config(text=f"Student added: {response.json()['name']}")
    else:
        result_label.config(text="Error adding student")
def submit_course():
    name = course_name_entry.get()
    level = course_level_entry.get()
    response = requests.post(API_URL_COURSE, json={"name": name, "level": level})
    if response.status_code == 201:
        course_result_label.config(text=f"Course added: {response.json()['name']}")
    else:
        course_result_label.config(text="Error adding course")
# Create the main window
root = tk.Tk()
root.title("Student and Course Registration")
# Student Registration
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Student Email:").pack()  # Added label for email
email_entry = tk.Entry(root)  # Added entry for email
email_entry.pack()
submit_button = tk.Button(root, text="Submit Student", command=submit_student)
submit_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
# Course Registration
tk.Label(root, text="Course Name:").pack()
course_name_entry = tk.Entry(root)
course_name_entry.pack()
tk.Label(root, text="Course Level:").pack()
course_level_entry = tk.Entry(root)
course_level_entry.pack()
submit_course_button = tk.Button(root, text="Submit Course", command=submit_course)
submit_course_button.pack()
course_result_label = tk.Label(root, text="")
course_result_label.pack()
# Start the GUI main loop
root.mainloop()