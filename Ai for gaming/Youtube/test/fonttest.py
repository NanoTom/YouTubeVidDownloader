import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Bold Text on Button Example")

# Create a button
bold = ('Arial', 12, 'bold')
#button = ttk.Button(root, text="Click Me", font=custom)
button = tk.Button(root, text="START" , width=15, height=2, font = bold)

# Create a bold font for the button text
bold_font = ('Arial', 12, 'bold')  # Font family, size, and weight (bold)

button.pack()
# Set the button text font to bold

# Start the Tkinter event loop
root.mainloop()
