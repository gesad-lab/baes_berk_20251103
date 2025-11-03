'''
Implements the GUI using Tkinter for user interaction and runs the FastAPI application.
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
        self.label = tk.Label(root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_student)
        self.submit_button.pack()
        self.get_button = tk.Button(root, text="Get Student", command=self.get_student)
        self.get_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    def submit_student(self):
        name = self.entry.get()
        response = requests.post(API_URL, json={"name": name})
        if response.status_code == 200:
            messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add student.")
    def get_student(self):
        student_id = self.entry.get()
        response = requests.get(API_URL + student_id)
        if response.status_code == 200:
            student = response.json()
            self.result_label.config(text=f"Student ID: {student['id']}, Name: {student['name']}")
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