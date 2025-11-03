'''
Implements the GUI for user interaction.
'''
import tkinter as tk
import requests
from alembic import command
from alembic.config import Config
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    raise ImportError("tkinter module is not available. Please install it to run the GUI.")
def run_migrations():
    alembic_cfg = Config("alembic.ini")  # Ensure you have an alembic.ini file
    command.upgrade(alembic_cfg, "head")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        # Student section
        self.label_name = tk.Label(master, text="Enter Student Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        self.add_student_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_student_button.pack()
        # Course section
        self.label_course_name = tk.Label(master, text="Enter Course Name:")
        self.label_course_name.pack()
        self.entry_course_name = tk.Entry(master)
        self.entry_course_name.pack()
        self.label_course_level = tk.Label(master, text="Enter Course Level:")
        self.label_course_level.pack()
        self.entry_course_level = tk.Entry(master)
        self.entry_course_level.pack()
        self.add_course_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        # Teacher section
        self.label_teacher_name = tk.Label(master, text="Enter Teacher Name:")
        self.label_teacher_name.pack()
        self.entry_teacher_name = tk.Entry(master)
        self.entry_teacher_name.pack()
        self.label_teacher_email = tk.Label(master, text="Enter Teacher Email:")
        self.label_teacher_email.pack()
        self.entry_teacher_email = tk.Entry(master)
        self.entry_teacher_email.pack()
        self.add_teacher_button = tk.Button(master, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.show_button = tk.Button(master, text="Show Students", command=self.show_students)
        self.show_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error adding student: {response.json().get('detail', 'Unknown error')}\n")
    def add_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Course: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error adding course: {response.json().get('detail', 'Unknown error')}\n")
    def add_teacher(self):
        name = self.entry_teacher_name.get()
        email = self.entry_teacher_email.get()
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Teacher: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error adding teacher: {response.json().get('detail', 'Unknown error')}\n")
    def show_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")
        else:
            self.output.insert(tk.END, "Error retrieving students\n")
if __name__ == "__main__":
    run_migrations()  # Run migrations before starting the GUI
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()