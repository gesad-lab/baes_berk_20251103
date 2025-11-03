'''
Graphical User Interface for the application using Tkinter.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, master):
        '''
        Initialize the GUI components.
        '''
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
        Add a new student by sending a request to the FastAPI server.
        '''
        name = self.entry.get()
        try:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            if response.status_code == 201:
                self.response_label.config(text="Student added successfully!")
            else:
                self.response_label.config(text="Error adding student.")
        except requests.exceptions.RequestException as e:
            self.response_label.config(text=f"Request failed: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()