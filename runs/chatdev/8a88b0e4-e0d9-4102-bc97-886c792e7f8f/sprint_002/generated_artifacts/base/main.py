'''
Simple GUI for interacting with the FastAPI application using Tkinter.
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
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
    def add_student(self):
        name = self.entry.get()
        if not name.strip():  # Validate that the name is not empty
            self.result_label.config(text="Name cannot be empty.")
            return
        try:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            response.raise_for_status()  # Raise an error for bad responses
            self.result_label.config(text=f"Student '{name}' added successfully!")
        except requests.exceptions.RequestException as e:
            self.result_label.config(text=f"Failed to add student: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()