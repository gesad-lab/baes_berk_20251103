'''
Tkinter GUI for interacting with the FastAPI application.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, root):
        '''
        Initialize the Tkinter GUI components.
        '''
        self.root = root
        self.root.title("Student Management")
        # Student management components
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.fetch_button = tk.Button(root, text="Fetch Students", command=self.fetch_students)
        self.fetch_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
        # Course management components
        self.course_name_label = tk.Label(root, text="Course Name:")
        self.course_name_label.pack()
        self.course_name_entry = tk.Entry(root)
        self.course_name_entry.pack()
        self.course_level_label = tk.Label(root, text="Course Level:")
        self.course_level_label.pack()
        self.course_level_entry = tk.Entry(root)
        self.course_level_entry.pack()
        self.add_course_button = tk.Button(root, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        # Teacher management components
        self.teacher_name_label = tk.Label(root, text="Teacher Name:")
        self.teacher_name_label.pack()
        self.teacher_name_entry = tk.Entry(root)
        self.teacher_name_entry.pack()
        self.teacher_email_label = tk.Label(root, text="Teacher Email:")
        self.teacher_email_label.pack()
        self.teacher_email_entry = tk.Entry(root)
        self.teacher_email_entry.pack()
        self.add_teacher_button = tk.Button(root, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.fetch_teachers_button = tk.Button(root, text="Fetch Teachers", command=self.fetch_teachers)
        self.fetch_teachers_button.pack()
        self.teachers_list = tk.Listbox(root)
        self.teachers_list.pack()
    def add_student(self):
        '''
        Add a new student by sending a POST request to the FastAPI application.
        '''
        name = self.name_entry.get()
        email = self.email_entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.fetch_students()
        else:
            print(f"Error adding student: {response.status_code} - {response.text}")  # Notify user of the error
    def fetch_students(self):
        '''
        Fetch the list of students by sending a GET request to the FastAPI application.
        '''
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, f"{student['id']} - {student['name']} - {student['email']}")
        else:
            print(f"Error fetching students: {response.status_code} - {response.text}")  # Notify user of the error
    def add_course(self):
        '''
        Add a new course by sending a POST request to the FastAPI application.
        '''
        name = self.course_name_entry.get()
        level = self.course_level_entry.get()
        selected_student = self.students_list.curselection()
        if selected_student:
            student_index = selected_student[0]
            student = self.students_list.get(student_index)
            student_id = student.split(" - ")[0]
            response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level, "student_id": student_id})
            if response.status_code == 200:
                self.course_name_entry.delete(0, tk.END)
                self.course_level_entry.delete(0, tk.END)
            else:
                print(f"Error adding course: {response.status_code} - {response.text}")  # Notify user of the error
    def add_teacher(self):
        '''
        Add a new teacher by sending a POST request to the FastAPI application.
        '''
        name = self.teacher_name_entry.get()
        email = self.teacher_email_entry.get()
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.teacher_name_entry.delete(0, tk.END)
            self.teacher_email_entry.delete(0, tk.END)
            self.fetch_teachers()
        else:
            print(f"Error adding teacher: {response.status_code} - {response.text}")  # Notify user of the error
    def fetch_teachers(self):
        '''
        Fetch the list of teachers by sending a GET request to the FastAPI application.
        '''
        self.teachers_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/teachers/")
        if response.status_code == 200:
            teachers = response.json()
            for teacher in teachers:
                self.teachers_list.insert(tk.END, f"{teacher['id']} - {teacher['name']} - {teacher['email']}")
        else:
            print(f"Error fetching teachers: {response.status_code} - {response.text}")  # Notify user of the error
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()