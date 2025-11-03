'''
Implements the GUI using Tkinter for user interaction.
'''
try:
    import tkinter as tk
    import requests  # Added import for requests
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
# Check if Tkinter is installed and provide instructions if not
try:
    import tkinter
except ImportError:
    print("Tkinter is not installed. Please install it to run the GUI.")
    exit(1)
# Added a check to ensure Tkinter is available before proceeding
if not tkinter:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        # Student Entry
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")  # Added email label
        self.label_email.pack()
        self.entry_email = tk.Entry(master)  # Added email entry
        self.entry_email.pack()
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
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()  # Get email input
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Updated to send email
        if response.status_code == 200:
            self.result_label.config(text=f"Student added: {response.json()['name']} with email: {response.json()['email']}")
        else:
            self.result_label.config(text="Error adding student")
    def add_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})  # Send course data
        if response.status_code == 200:
            self.result_course_label.config(text=f"Course added: {response.json()['name']} with level: {response.json()['level']}")
        else:
            self.result_course_label.config(text="Error adding course")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()