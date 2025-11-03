'''
Implements a simple GUI using Tkinter to interact with the FastAPI application.
'''
try:
    import tkinter as tk
    import requests
except ImportError:
    print("Tkinter is not installed. Please install it to use the GUI.")
    exit(1)
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Application")
        # Student section
        self.label_name = tk.Label(master, text="Enter Student Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        self.label_courses = tk.Label(master, text="Enter Course IDs (comma-separated):")
        self.label_courses.pack()
        self.entry_courses = tk.Entry(master)
        self.entry_courses.pack()
        self.submit_button = tk.Button(master, text="Submit Student", command=self.submit_student)
        self.submit_button.pack()
        self.response_label = tk.Label(master, text="")
        self.response_label.pack()
        # Teacher section
        self.label_teacher_name = tk.Label(master, text="Enter Teacher Name:")
        self.label_teacher_name.pack()
        self.entry_teacher_name = tk.Entry(master)
        self.entry_teacher_name.pack()
        self.label_teacher_email = tk.Label(master, text="Enter Teacher Email:")
        self.label_teacher_email.pack()
        self.entry_teacher_email = tk.Entry(master)
        self.entry_teacher_email.pack()
        self.submit_teacher_button = tk.Button(master, text="Submit Teacher", command=self.submit_teacher)
        self.submit_teacher_button.pack()
        self.teacher_response_label = tk.Label(master, text="")
        self.teacher_response_label.pack()
        # Course section
        self.label_course_name = tk.Label(master, text="Enter Course Name:")
        self.label_course_name.pack()
        self.entry_course_name = tk.Entry(master)
        self.entry_course_name.pack()
        self.label_course_level = tk.Label(master, text="Enter Course Level:")
        self.label_course_level.pack()
        self.entry_course_level = tk.Entry(master)
        self.entry_course_level.pack()
        self.label_teacher_id = tk.Label(master, text="Enter Teacher ID for Course:")
        self.label_teacher_id.pack()
        self.entry_teacher_id = tk.Entry(master)
        self.entry_teacher_id.pack()
        self.submit_course_button = tk.Button(master, text="Submit Course", command=self.submit_course)
        self.submit_course_button.pack()
        self.course_response_label = tk.Label(master, text="")
        self.course_response_label.pack()
    def submit_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        course_ids = [int(x.strip()) for x in self.entry_courses.get().split(',')] if self.entry_courses.get() else []
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email, "course_ids": course_ids})
        if response.status_code == 200:
            self.response_label.config(text="Student added successfully!")
        else:
            self.response_label.config(text="Error adding student.")
    def submit_teacher(self):
        name = self.entry_teacher_name.get()
        email = self.entry_teacher_email.get()
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.teacher_response_label.config(text="Teacher added successfully!")
        else:
            self.teacher_response_label.config(text="Error adding teacher.")
    def submit_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        teacher_id = int(self.entry_teacher_id.get()) if self.entry_teacher_id.get() else None
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level, "teacher_id": teacher_id})
        if response.status_code == 200:
            self.course_response_label.config(text="Course added successfully!")
        else:
            self.course_response_label.config(text="Error adding course.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()