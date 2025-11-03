'''
Implements the GUI using Tkinter for user interaction.
'''
try:
    import tkinter as tk
    import requests
except ImportError:
    print("Tkinter or requests is not installed. Please install them to run the GUI.")
    exit()
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
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
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
        # Enroll Entry
        self.label_student_id = tk.Label(master, text="Enter Student ID to Enroll:")
        self.label_student_id.pack()
        self.entry_student_id = tk.Entry(master)
        self.entry_student_id.pack()
        self.label_course_id = tk.Label(master, text="Enter Course ID to Enroll:")
        self.label_course_id.pack()
        self.entry_course_id = tk.Entry(master)
        self.entry_course_id.pack()
        self.enroll_button = tk.Button(master, text="Enroll Student in Course", command=self.enroll_student_in_course)
        self.enroll_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error: {response.text}\n")
    def add_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Course: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error: {response.text}\n")
    def add_teacher(self):
        name = self.entry_teacher_name.get()
        email = self.entry_teacher_email.get()
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Teacher: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error: {response.text}\n")
    def enroll_student_in_course(self):
        student_id = self.entry_student_id.get()
        course_id = self.entry_course_id.get()
        response = requests.post(f"http://127.0.0.1:8000/students/{student_id}/courses/{course_id}/enroll")
        if response.status_code == 200:
            self.output.insert(tk.END, f"Enrolled Student in Course: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error: {response.text}\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()