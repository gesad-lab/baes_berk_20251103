'''
Implements the GUI for user interaction using Tkinter.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def submit(self):
        name = self.entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Student created: {response.json()}\n")
        else:
            self.output.insert(tk.END, f"Error: {response.text}\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()