'''
Simple GUI for interacting with the FastAPI backend.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, root):
        '''
        Initialize the GUI components.
        '''
        self.root = root
        self.root.title("Student Management")
        self.label = tk.Label(root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    def add_student(self):
        '''
        Add a student by sending a POST request to the FastAPI backend.
        '''
        name = self.entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.result_label.config(text="Student added successfully!")
        else:
            self.result_label.config(text="Error adding student.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()