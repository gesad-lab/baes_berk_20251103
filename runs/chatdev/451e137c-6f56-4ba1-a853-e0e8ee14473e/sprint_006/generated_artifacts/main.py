'''
Defines the GUI for the Student, Course, and Teacher Management application.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    print("Error: tkinter module is not installed. Please install it to run the application.")
    exit(1)
# Ensure tkinter is installed
try:
    import tkinter
except ImportError:
    print("Error: tkinter module is not installed. Please install it to run the application.")
    exit(1)
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student, Course, and Teacher Management")
        # Student section
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.email_label = tk.Label(master, text="Enter Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(master)
        self.email_entry.pack()
        self.add_student_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_student_button.pack()
        # Course section
        self.course_label = tk.Label(master, text="Enter Course Name:")
        self.course_label.pack()
        self.course_entry = tk.Entry(master)
        self.course_entry.pack()
        self.level_label = tk.Label(master, text="Enter Course Level:")
        self.level_label.pack()
        self.level_entry = tk.Entry(master)
        self.level_entry.pack()
        # Teacher selection
        self.teacher_label = tk.Label(master, text="Select Teacher ID:")
        self.teacher_label.pack()
        self.teacher_entry = tk.Entry(master)
        self.teacher_entry.pack()
        self.add_course_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        # Teacher section
        self.teacher_name_label = tk.Label(master, text="Enter Teacher Name:")
        self.teacher_name_label.pack()
        self.teacher_name_entry = tk.Entry(master)
        self.teacher_name_entry.pack()
        self.teacher_email_label = tk.Label(master, text="Enter Teacher Email:")
        self.teacher_email_label.pack()
        self.teacher_email_entry = tk.Entry(master)
        self.teacher_email_entry.pack()
        self.add_teacher_button = tk.Button(master, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.display_button = tk.Button(master, text="Display Students", command=self.display_students)
        self.display_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.email_entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {name} with Email: {email}\n")
        else:
            self.output.insert(tk.END, "Error adding student\n")
    def add_course(self):
        name = self.course_entry.get()
        level = self.level_entry.get()
        teacher_id = self.teacher_entry.get()  # Get teacher_id from entry
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level, "teacher_id": teacher_id})  # Send teacher_id
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Course: {name} with Level: {level}\n")
        else:
            self.output.insert(tk.END, "Error adding course\n")
    def add_teacher(self):
        name = self.teacher_name_entry.get()
        email = self.teacher_email_entry.get()
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Teacher: {name} with Email: {email}\n")
        else:
            self.output.insert(tk.END, "Error adding teacher\n")
    def display_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}\n")
        else:
            self.output.insert(tk.END, "Error retrieving students\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()