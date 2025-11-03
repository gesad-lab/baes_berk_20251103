'''
Implements the FastAPI application and the graphical user interface using Tkinter.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router  # Import the router
import tkinter as tk
from tkinter import messagebox
import requests
app = FastAPI()
# Allow CORS for the GUI to interact with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as necessary for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include the router
app.include_router(router)
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration")
        self.label = tk.Label(root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_student)
        self.submit_button.pack()
    def submit_student(self):
        name = self.entry.get()
        if name:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            if response.status_code == 201:
                messagebox.showinfo("Success", "Student registered successfully!")
            else:
                messagebox.showerror("Error", "Failed to register student.")
        else:
            messagebox.showwarning("Warning", "Name cannot be empty.")
if __name__ == "__main__":
    import uvicorn
    # Initialize the database
    from database import init_db
    init_db()  # Create the database schema automatically on startup
    # Run the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # Start the Tkinter GUI
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()