'''
Implements the GUI using Tkinter for user interaction.
'''
import tkinter as tk
from tkinter import messagebox
import requests
class CourseApp:
    def __init__(self, master):
        self.master = master
        master.title("Course Management")
        self.label = tk.Label(master, text="Course Management")
        self.label.pack()
        self.name_label = tk.Label(master, text="Course Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()
        self.level_label = tk.Label(master, text="Course Level:")
        self.level_label.pack()
        self.level_entry = tk.Entry(master)
        self.level_entry.pack()
        self.create_button = tk.Button(master, text="Create Course", command=self.create_course)
        self.create_button.pack()
        self.courses_button = tk.Button(master, text="View Courses", command=self.view_courses)
        self.courses_button.pack()
        self.courses_list = tk.Listbox(master)
        self.courses_list.pack()
    def create_course(self):
        name = self.name_entry.get()
        level = self.level_entry.get()
        if not name or not level:
            messagebox.showerror("Input Error", "Both fields are required.")
            return
        response = requests.post("http://localhost:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            messagebox.showinfo("Success", "Course created successfully!")
            self.name_entry.delete(0, tk.END)
            self.level_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", response.json().get("detail", "An error occurred."))
    def view_courses(self):
        response = requests.get("http://localhost:8000/courses/")
        if response.status_code == 200:
            self.courses_list.delete(0, tk.END)
            for course in response.json():
                self.courses_list.insert(tk.END, f"{course['name']} - {course['level']}")
        else:
            messagebox.showerror("Error", "Failed to retrieve courses.")