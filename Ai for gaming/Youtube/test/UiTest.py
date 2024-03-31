import tkinter as tk
from tkinter import filedialog

def open_folder_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open the Windows Explorer dialog for selecting a folder
    folder_path = filedialog.askdirectory()
    return folder_path

if __name__ == "__main__":
    selected_folder = open_folder_dialog()
    if selected_folder:
        print("Selected folder:", selected_folder)
    else:
        print("No folder selected.")