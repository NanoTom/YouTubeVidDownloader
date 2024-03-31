import tkinter as tk
import random

def move_button(event):
    print("no been touched")
    #randomly changes the dimensions of the button no whenever the user hovers over it
    new_x = random.randint(0, root.winfo_width() - button.winfo_reqwidth())
    new_y = random.randint(0, root.winfo_height() - button.winfo_reqheight())
    no.place(x=new_x, y=new_y)



def said_yes():
    #properties of second window
    new_window = tk.Toplevel(root)
    new_window.title("Yes??")
    new_window.geometry("250x100")

    #The font and size and message of the new window display message
    message_font = ("Arial", 18, "bold")
    message_label = tk.Label(new_window , text = "Kill yourself", font=message_font)
    message_label.pack()

root = tk.Tk()
root.title("Gay test")
root.geometry("400x300")


w = tk.Label(root, text="Are you gay?")
w.place(x = 150, y = 50)

# Wait until the window is updated to get its dimensions
root.update_idletasks()

no = button = tk.Button(root, text="No")
no.place(x = 200,y=100)
# Bind the <Enter> event to the button
no.bind("<Enter>", move_button)  #runs whenever the user hovers over this particular button




yes = button = tk.Button(root, text="Yes", command=lambda:said_yes())
yes.place(x = 125,y=100)
yes.bind("<Enter>", print("Been touched"))

root.mainloop()
