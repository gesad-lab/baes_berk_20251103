'''
Implements a simple GUI using Tkinter to interact with the FastAPI backend.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it to run the GUI.")
    exit()
import requests
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        # Student section
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.email_label = tk.Label(master, text="Enter Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(master)
        self.email_entry.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.response_label = tk.Label(master, text="")
        self.response_label.pack()
        # Teacher section
        self.teacher_label = tk.Label(master, text="Enter Teacher Name:")
        self.teacher_label.pack()
        self.teacher_entry = tk.Entry(master)
        self.teacher_entry.pack()
        self.teacher_email_label = tk.Label(master, text="Enter Teacher Email:")
        self.teacher_email_label.pack()
        self.teacher_email_entry = tk.Entry(master)
        self.teacher_email_entry.pack()
        self.add_teacher_button = tk.Button(master, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.teacher_response_label = tk.Label(master, text="")
        self.teacher_response_label.pack()
    def add_student(self):
        '''
        Sends a request to add a student to the FastAPI backend.
        '''
        name = self.entry.get()
        email = self.email_entry.get()  # Get the email from the entry
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.response_label.config(text="Student added successfully!")
        else:
            self.response_label.config(text="Error adding student.")
    def add_teacher(self):
        '''
        Sends a request to add a teacher to the FastAPI backend.
        '''
        name = self.teacher_entry.get()
        email = self.teacher_email_entry.get()  # Get the email from the entry
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.teacher_response_label.config(text="Teacher added successfully!")
        else:
            self.teacher_response_label.config(text="Error adding teacher.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()