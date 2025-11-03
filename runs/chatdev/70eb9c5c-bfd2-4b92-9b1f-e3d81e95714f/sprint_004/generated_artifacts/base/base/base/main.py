'''
Simple GUI application to interact with the Student API.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.submit_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()['name']}\n")
        else:
            self.output.insert(tk.END, "Error adding student\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()