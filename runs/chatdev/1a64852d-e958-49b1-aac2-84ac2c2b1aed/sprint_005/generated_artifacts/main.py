'''
Graphical User Interface for managing courses.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
except ImportError:
    print("Tkinter is not installed. Please install it to run the GUI.")
    exit(1)
class CourseApp:
    def __init__(self, master):
        self.master = master
        master.title("Course Management")
        self.label_name = tk.Label(master, text="Enter Course Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()
        self.label_level = tk.Label(master, text="Enter Course Level:")
        self.label_level.pack()
        self.entry_level = tk.Entry(master)
        self.entry_level.pack()
        self.add_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.add_button.pack()
        self.show_button = tk.Button(master, text="Show Courses", command=self.show_courses)
        self.show_button.pack()
        self.courses_list = tk.Listbox(master)
        self.courses_list.pack()
    def add_course(self):
        name = self.entry_name.get()
        level = self.entry_level.get()
        if name and level:
            response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Course added successfully!")
                self.entry_name.delete(0, tk.END)
                self.entry_level.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to add course.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and level.")
    def show_courses(self):
        self.courses_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/courses/")
        if response.status_code == 200:
            courses = response.json()
            for course in courses:
                self.courses_list.insert(tk.END, f"{course['id']}: {course['name']} - {course['level']}")  # Show course details
if __name__ == "__main__":
    root = tk.Tk()
    app = CourseApp(root)
    root.mainloop()