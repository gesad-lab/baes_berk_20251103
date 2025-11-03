'''
Implements the GUI using Tkinter for user interaction.
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
        self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    def add_student(self):
        name = self.name_entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.result_label.config(text=f"Student added: {response.json()['name']}")
        else:
            self.result_label.config(text="Error adding student")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()