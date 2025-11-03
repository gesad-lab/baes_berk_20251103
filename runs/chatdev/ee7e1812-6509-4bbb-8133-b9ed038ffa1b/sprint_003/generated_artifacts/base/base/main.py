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
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.show_button = tk.Button(root, text="Show Students", command=self.show_students)
        self.show_button.pack()
        self.output_text = tk.Text(root)
        self.output_text.pack()
    def add_student(self):
        '''
        Adds a new student by sending a POST request to the API.
        '''
        name = self.name_entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.output_text.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output_text.insert(tk.END, "Failed to add student\n")
    def show_students(self):
        '''
        Retrieves and displays the list of students from the API.
        '''
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output_text.delete(1.0, tk.END)
            for student in students:
                self.output_text.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}\n")
        else:
            self.output_text.insert(tk.END, "Failed to retrieve students\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()