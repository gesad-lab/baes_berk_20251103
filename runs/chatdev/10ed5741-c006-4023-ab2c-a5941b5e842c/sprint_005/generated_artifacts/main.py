'''
User interface for the Student Management application using Tkinter.
'''
try:
    import tkinter as tk
    import requests
except ImportError:
    print("Tkinter or requests is not installed. Please install them to run the GUI.")
    exit(1)
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        # Student Entry
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        self.label_courses = tk.Label(master, text="Enter Course IDs (comma-separated):")
        self.label_courses.pack()
        self.entry_courses = tk.Entry(master)
        self.entry_courses.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        # Course Entry
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
        self.result_course_label = tk.Label(master, text="")
        self.result_course_label.pack()
        # Teacher Entry
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
        self.result_teacher_label = tk.Label(master, text="")
        self.result_teacher_label.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()
        course_ids = self.entry_courses.get().split(",")
        course_ids = [int(course_id.strip()) for course_id in course_ids if course_id.strip().isdigit()]
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email, "course_ids": course_ids})
        if response.status_code == 200:
            self.result_label.config(text=f"Student added: {response.json()['name']} with email: {response.json()['email']}")
        else:
            self.result_label.config(text="Error adding student")
    def add_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.result_course_label.config(text=f"Course added: {response.json()['name']} with level: {response.json()['level']}")
        else:
            self.result_course_label.config(text="Error adding course")
    def add_teacher(self):
        name = self.entry_teacher_name.get()
        email = self.entry_teacher_email.get()
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.result_teacher_label.config(text=f"Teacher added: {response.json()['name']} with email: {response.json()['email']}")
        else:
            self.result_teacher_label.config(text="Error adding teacher")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()