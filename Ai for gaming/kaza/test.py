import tkinter as tk
from PIL import ImageTk, Image

# Create the main window
window = tk.Tk()
window.title("Toggle Image Example")

# Load the image
image_path = "skull.png"
image = Image.open(image_path)
image = image.resize((200, 200), Image.LANCZOS)  # Resize the image with anti-aliasing using LANCZOS filter
tk_image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(window, image=tk_image)

# Function to toggle image visibility
def toggle_image():
    if image_label.winfo_ismapped():  # Check if the image label is currently visible
        image_label.pack_forget()  # Hide the image label if visible
    else:
        image_label.pack()  # Display the image label if hidden

# Create a button to toggle the image
toggle_button = tk.Button(window, text="Toggle Image", command=toggle_image)

# Pack the button
toggle_button.pack()

# Run the main event loop
window.mainloop()
