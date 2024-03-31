#total time spent on this code including test and everything is in hours:
#3.5
import time
import tkinter as tk
from tkinter import ttk
from pytube import YouTube


#to make the function wait for other functions to finish first
import threading
lock = threading.Lock()


#for explorer
from tkinter import filedialog

#for default download path to be downloads:
import os


#for image
from PIL import Image, ImageTk

#functions
#function for placeholder to disappear when clicked and come back when leave


#function is ready or not
global ready
ready = False

#Default values if any:
homedirectory = os.path.expanduser('~')
global path
path = os.path.join(homedirectory,'Downloads')

global resolution
resolution = '480p'

items_list = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]


##temp idk this:
def handle_selection(selected_item, window):
    print("Starting handle selection")
    global resolution
    global ready
    if window == new_window:  # Check if the function is called from the new window
        print(f"Selected item: {selected_item}")
        resolution = selected_item
        ready = True
        window.destroy()  # Close the window

def open_new_window(ListOfRes):
    print("Starting open new window")
    items_list = ListOfRes
    global new_window  # Declare new_window as global so it can be accessed and modified
    new_window = tk.Toplevel(root)  # Create a new toplevel window
    new_window.title("New Window")


    print("Checkpoint 1")
    # Create a label in the new window


    label = ttk.Label(new_window, text="Select an item in the new window:")
    label.pack(padx=10, pady=5)

    print("Checkpoint 2")
    # Create a dropdown menu in the new window
    selected_item = tk.StringVar()
    dropdown = ttk.Combobox(new_window, textvariable=selected_item, values=items_list)
    dropdown.pack(padx=10, pady=5)

    print("Checkpoint 3")
    # Create a button in the new window to handle selection



    ################################ code temp edit
    select_button = ttk.Button(new_window, text="Select")
    select_button.config(command=lambda: handle_selection(selected_item.get(), new_window))
    select_button.pack(padx=10, pady=5)


    # select_button = ttk.Button(new_window, text="Select",
    #                            command=lambda: handle_selection(selected_item.get(), new_window))
    # select_button.pack(padx=10, pady=5)

    print("End of the function")

def on_entry_click(event):
    if input_entry.get() == "Past the link here":
        input_entry.delete(0,tk.END)
        input_entry.config(foreground='black')

def on_entry_leave(event):
    if input_entry.get() == "":
        input_entry.insert(0,"Past the link here")
        input_entry.config(foreground ='grey')



#function to get input from input entry
def get_input():
    user_input = input_entry.get()
    download_video(user_input)


#focuses back into the main window
def unselect_entry(event):
    if event.widget != input_entry:
        root.focus()


def GetPath():
    global path
    # Open the Windows Explorer dialog for selecting a folder
    path = filedialog.askdirectory()
    print(path)


## resolution finder
def GetResolutions(yt):
    with lock:
        list = []
        streams = yt.streams.filter()
        unique = set()  # what is a set??

        for stream in streams:
            if stream.resolution:
                unique.add((stream.resolution))

        print("Available options:")
        for resolution in unique:
            print(f"Resolution: {resolution}")
            list.append(resolution)

        open_new_window(list)##idk wht to do with this wait
    # which = str(input("Which resolution you want?")) +'p'
    #
    # try:
    #     print(list)
    #     index = list.index(which)
    #     res = list[index]
    #     print("The desired Resolution is:", res)
    #     return res
    #
    # except ValueError:
    #     print("Did nat find")


#Main downloader functions:
def download_video(youtube_url):
    global ready

    time.sleep(0.5)
    yt = YouTube(youtube_url)  # this gets the vide
    print("The Current video is:", yt.title)

    GetResolutions(yt)

    # line removed

    while True:
        while ready:
            global path #path of download that user choice
            global resolution

            try:
                #print with desired resolution
                video = yt.streams.filter(res=resolution).first()

                video.download(output_path=path) #this straight forward
                print("Video downloaded successfully. with resolution:", resolution)
                ready = False

            except Exception as e:
                print(f"Error downloading video: {e}")



# Create the main window
root = tk.Tk()
root.title("Ui Prototype")


#dimentions of the ui
root.geometry("600x400")

# Add widgets or functionality here...

image = Image.open("YouLogo.png")
image = image.resize((200, 100))  # Resize the image as needed
photo = ImageTk.PhotoImage(image)

# Create a label for the image
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=0, padx=0, pady=10)  # Adjust padx and pady as needed

# Create a label for the bold text
bold_text_label = tk.Label(root, text="DOWNLOADER", font=("Arial", 24, "bold"))
bold_text_label.grid(row=0, column=1, padx=10, pady=10)


#take input + placeholder:
placeholder_text = "Past the link here"
input_entry = ttk.Entry(root, width=40)
input_entry.insert(0,placeholder_text)
input_entry.config(foreground='grey')
input_entry.bind('<FocusIn>', on_entry_click)
input_entry.bind('<FocusOut>', on_entry_leave)
input_entry.place(relx=0.5, rely=0.5, anchor='center',height=30)



#windows explorer button to select the path of download
ExplorerLogo = tk.PhotoImage(file= "explorer.png")
ExplorerLogo = ExplorerLogo.subsample(2,2)

ExplorerButton = tk.Button(root, image = ExplorerLogo, command=GetPath,width=25, height=25)
ExplorerButton.place(relx=0.75, rely=0.5, anchor='center')




#Start button
#Our start button working now with custom ui
#Start_button = ttk.Button(root, text = "Start", command=get_input, width=20)
bold =('Arial', 12, 'bold')
Start_button = tk.Button(root, text="START",command= get_input, width=15, height=2, font = bold)
Start_button.place(relx=0.5, rely=0.61, anchor='center')
#Start_button.config(font = ('Arial', 12, 'bold'))


#input_button = ttk.Button(root, text= "Get Input", command = get_input())

root.bind('<Button-1>', unselect_entry)

# Start the Tkinter event loop
root.mainloop()











#
# resolution_label = tk.Label(root, text="Select Resolution:")
# resolution_label.pack()
#
# resolutions = ['720p', '480p', '360p', '240p', '144p']
# resolution_combobox = ttk.Combobox(root, values=resolutions)
# resolution_combobox.pack()
#
# download_button = tk.Button(root, text="Download", command=download_video)
# download_button.pack()
#
# result_label = tk.Label(root, text="")
# result_label.pack()
#
# # Start the Tkinter event loop
# root.mainloop()
