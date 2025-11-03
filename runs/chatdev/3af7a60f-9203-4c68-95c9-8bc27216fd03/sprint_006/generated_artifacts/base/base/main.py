'''
Main GUI for the Student and Course Management application.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    print("tkinter module is not available. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student and Course Management")
        # Student Input
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
        self.submit_button = tk.Button(master, text="Submit Student", command=self.submit_student)
        self.submit_button.pack()
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        # Course Input
        self.label_course_name = tk.Label(master, text="Enter Course Name:")
        self.label_course_name.pack()
        self.entry_course_name = tk.Entry(master)
        self.entry_course_name.pack()
        self.label_course_level = tk.Label(master, text="Enter Course Level:")
        self.label_course_level.pack()
        self.entry_course_level = tk.Entry(master)
        self.entry_course_level.pack()
        self.submit_course_button = tk.Button(master, text="Submit Course", command=self.submit_course)
        self.submit_course_button.pack()
        self.result_course_label = tk.Label(master, text="")
        self.result_course_label.pack()
    def submit_student(self):
        name = self.entry.get()
        email = self.entry_email.get()
        courses = list(map(int, self.entry_courses.get().split(',')))  # Convert input to list of integers
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email, "courses": courses})
        if response.status_code == 200:
            self.result_label.config(text=f"Student {name} added successfully!")
        else:
            self.result_label.config(text="Error adding student.")
    def submit_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.result_course_label.config(text=f"Course {name} added successfully!")
        else:
            self.result_course_label.config(text="Error adding course.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()