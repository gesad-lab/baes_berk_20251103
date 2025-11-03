'''
Main GUI for the Student Management application.
'''
import tkinter as tk
from tkinter import messagebox
import requests
import threading
from uvicorn import run
from app import app  # Import the FastAPI app
API_URL = "http://127.0.0.1:8000/students/"
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
        self.get_button = tk.Button(root, text="Get Student", command=self.get_student)
        self.get_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    def submit_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        response = requests.post(API_URL, json={"name": name, "email": email})  # Include email in request
        if response.status_code == 200:
            messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add student.")
    def get_student(self):
        student_id = self.entry_name.get()  # Assuming student ID is entered in the name field
        response = requests.get(API_URL + student_id)
        if response.status_code == 200:
            student = response.json()
            self.result_label.config(text=f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}")
        else:
            messagebox.showerror("Error", "Student not found.")
def run_fastapi():
    run(app, host="127.0.0.1", port=8000)
if __name__ == "__main__":
    # Start FastAPI in a separate thread
    threading.Thread(target=run_fastapi, daemon=True).start()
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()