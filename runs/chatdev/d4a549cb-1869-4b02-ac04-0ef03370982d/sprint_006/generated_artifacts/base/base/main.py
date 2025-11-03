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
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.response_label = tk.Label(master, text="")
        self.response_label.pack()
    def submit(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        course_ids = [int(x.strip()) for x in self.entry_courses.get().split(',')] if self.entry_courses.get() else []
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email, "course_ids": course_ids})
        if response.status_code == 200:
            self.response_label.config(text="Student added successfully!")
        else:
            self.response_label.config(text="Error adding student.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()