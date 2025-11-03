'''
Contains the GUI implementation using Tkinter.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.label_name = tk.Label(root, text="Enter Student Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()
        self.label_email = tk.Label(root, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_student)
        self.submit_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        self.fetch_button = tk.Button(root, text="Fetch Students", command=self.fetch_students)
        self.fetch_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
    def submit_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()  # Get email input
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Send email
        if response.status_code == 200:
            self.result_label.config(text=f"Student {name} added!")
        else:
            self.result_label.config(text="Error adding student.")
    def fetch_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.students_list.delete(0, tk.END)
            for student in students:
                self.students_list.insert(tk.END, f"{student['id']}: {student['name']} ({student['email']})")  # Show email
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()