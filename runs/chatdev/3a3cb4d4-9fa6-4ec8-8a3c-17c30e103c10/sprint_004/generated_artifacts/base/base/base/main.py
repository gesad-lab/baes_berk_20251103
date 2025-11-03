'''
Implements a simple GUI using Tkinter to interact with the FastAPI backend.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.response_label = tk.Label(master, text="")
        self.response_label.pack()
    def add_student(self):
        '''
        Sends a request to add a student to the FastAPI backend.
        '''
        name = self.entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.response_label.config(text="Student added successfully!")
        else:
            self.response_label.config(text="Error adding student.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()