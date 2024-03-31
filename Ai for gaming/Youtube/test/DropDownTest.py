import tkinter as tk
from tkinter import ttk

# Define the list of items for the dropdown menu
items_list = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]


def handle_selection(selected_item, window):
    if window == new_window:  # Check if the function is called from the new window
        print(f"Selected item: {selected_item}")
        window.destroy()  # Close the window


def open_new_window():
    global new_window  # Declare new_window as global so it can be accessed and modified
    new_window = tk.Toplevel(root)  # Create a new toplevel window
    new_window.title("New Window")

    # Create a label in the new window
    label = ttk.Label(new_window, text="Select an item in the new window:")
    label.pack(padx=10, pady=5)

    # Create a dropdown menu in the new window
    selected_item = tk.StringVar()
    dropdown = ttk.Combobox(new_window, textvariable=selected_item, values=items_list)
    dropdown.pack(padx=10, pady=5)

    # Create a button in the new window to handle selection
    select_button = ttk.Button(new_window, text="Select")
    select_button.config(command=lambda: handle_selection(selected_item.get(), new_window))
    select_button.pack(padx=10, pady=5)


# Create the main window
root = tk.Tk()
root.title("Dropdown Menu Example")

# Create a label
label = ttk.Label(root, text="Select an item:")
label.pack(padx=10, pady=5)

# Create a dropdown menu
selected_item = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_item, values=items_list)
dropdown.pack(padx=10, pady=5)

# Create a button to open a new window
open_window_button = ttk.Button(root, text="Open New Window", command=open_new_window)
open_window_button.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
