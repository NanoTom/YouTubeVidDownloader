import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Button with Image Example")
root.geometry("800x600")
# Load the image
image = tk.PhotoImage(file="YouLogo.png")  # Replace "path_to_your_image.png" with the actual path to your image
image = image.subsample(15,15)

# Create a button with the image
button = tk.Button(root, image=image, compound=tk.TOP, width=50, height = 50)
button.place(relx=0.5, rely=0.5, anchor='center')

# Start the Tkinter event loop
root.mainloop()
