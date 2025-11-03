'''
Graphical User Interface for the Student application.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    from course import create_course  # Import the create_course function
    class StudentApp:
        def __init__(self, master):
            self.master = master
            master.title("Student Application")
            # Additional GUI setup for Course creation
            self.course_name_label = tk.Label(master, text="Course Name:")
            self.course_name_label.pack()
            self.course_name_entry = tk.Entry(master)
            self.course_name_entry.pack()
            self.course_level_label = tk.Label(master, text="Course Level:")
            self.course_level_label.pack()
            self.course_level_entry = tk.Entry(master)
            self.course_level_entry.pack()
            self.add_course_button = tk.Button(master, text="Add Course", command=self.add_course)
            self.add_course_button.pack()
        def add_course(self):
            name = self.course_name_entry.get()
            level = self.course_level_entry.get()
            if name and level:
                create_course(db, name, level)  # Call create_course function
                messagebox.showinfo("Success", "Course added successfully!")
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields.")
except ImportError:
    print("Error: tkinter module is not available. Please install tkinter to run the GUI.")