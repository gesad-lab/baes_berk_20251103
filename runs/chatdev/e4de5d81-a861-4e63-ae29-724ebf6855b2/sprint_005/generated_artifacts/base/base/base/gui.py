'''
Simple GUI for interacting with the FastAPI backend using Tkinter.
'''
import tkinter as tk
import requests
API_URL = "http://127.0.0.1:8000/students/"
def create_student():
    name = name_entry.get()
    email = email_entry.get()
    response = requests.post(API_URL, json={"name": name, "email": email})
    if response.status_code == 200:
        result_label.config(text="Student created successfully!")
    else:
        result_label.config(text=f"Error creating student: {response.json().get('detail', 'Unknown error')}")
def get_students():
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        students_list.delete(0, tk.END)
        for student in students:
            students_list.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}")
# Create the main window
root = tk.Tk()
root.title("Student Management")
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
# Run the GUI loop
root.mainloop()