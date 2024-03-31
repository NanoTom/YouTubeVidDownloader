import pyautogui
import keyboard
import time
import tkinter as tk
import random
from PIL import ImageTk, Image


# Create the main window
window = tk.Tk()
window.title("Pedo Detector")
window.geometry("800x500")


#image input
skull = "skulll.png"
skull = Image.open(skull)


#universal fonts
bold = ("Arial",12,"bold")
bold2 = ("Arial",25,"bold")

# Intial label
label = tk.Label(window, text="Welcome to pedo Detector", font = bold)
label.place(relx=0.5, rely=0.4, anchor='center')


#intializing image without placing
tk_image = ImageTk.PhotoImage(skull)
imagelabel = tk.Label(window, image=tk_image)


#outputs whatever the main updater gives it and removes and updates the image
def update_label(alo):
    if alo == "All Clear":
        new_value = alo
        label.config(text=new_value, font=bold, fg="black")
        if imagelabel.winfo_ismapped():
            imagelabel.place_forget()

    else:
        new_value = alo
        label.config(text=new_value, font=bold2, fg="red")
        imagelabel.place(relx=0.5, rely=0.6, anchor='center')



#has the image reconition and runs the update_label
def updater():
    try:
        if pyautogui.locateOnScreen("Kaza.png", confidence = 0.6):
            update_label("Pedo Detected")
        else:
            update_label("All Clear")    #I believe works in other versions of pyautogui but as of now it does nothing

    except pyautogui.ImageNotFoundException:
        update_label("All Clear")

    window.after(1000, updater) #loops forever

button = tk.Button(window, text="START" , command=updater, width=15, height=2, font = bold)
button.place(x = 300,y = 400)


# Run the main event loop
window.mainloop()
