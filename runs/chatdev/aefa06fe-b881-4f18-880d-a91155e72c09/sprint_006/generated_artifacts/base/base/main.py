'''
Implements a simple GUI using Tkinter for user interaction.
'''
# Check if tkinter is available
try:
    import tkinter as tk
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")