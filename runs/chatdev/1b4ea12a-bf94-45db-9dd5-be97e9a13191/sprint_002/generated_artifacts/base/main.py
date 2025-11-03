'''
Simple GUI for interacting with the FastAPI backend.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
        self.fetch_students()
    def add_student(self):
        name = self.name_entry.get()
        if name:
            response = requests.post("http://127.0.0.1:8000/students", json={"name": name})
            if response.status_code == 201:
                self.fetch_students()
    def fetch_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, student['name'])
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()