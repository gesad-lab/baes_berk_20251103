'''
Implements the FastAPI application and the graphical user interface using Tkinter.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router  # Import the router
import requests
# Check if tkinter is available
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("tkinter module is not available. Please install it to use the GUI.")
    exit(1)
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
# Initialize the database
from database import init_db
init_db()  # Create the database schema automatically on startup
if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # Start the Tkinter GUI
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()