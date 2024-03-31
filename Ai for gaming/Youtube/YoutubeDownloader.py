from pytube import YouTube
import sys


import os #reason for import is to put default download directory as downloads for the user


#for ui and windows explorer
import tkinter as tk
from tkinter import filedialog

#my own switch statment for later use for the app
#skipped looked complicated will experient on its own later


#############################
#bugs found:
#if video already exists in a directory it says download successful anyways without trying


#setting default path
homedirectory = os.path.expanduser('~')
global path
path = os.path.join(homedirectory,'Downloads')


#introduction to the app
def intro():
    print("Welcome to basic youtube video dowloader")
    print("Press 1 to go to download")
    print("Press 2 to specify download path (if not specified it will go to default)")
    print("Press 3 to exit:")

    UserIntro = int(input("Enter your choice:"))

    if UserIntro == 1:
        return
    elif UserIntro ==2:
        GetPath()
    elif UserIntro ==3:
        print("Thank you")
        sys.exit()
    else:
        print("internal input error")
    return


def confirmation():
    confirm = input("Download (y/n)")
    confirm = confirm.lower()
    if confirm == 'y' or confirm == "yes":
        print("Will download")

    else:
        print("ty for using app")
        sys.exit()



#as it says
def GetResolutions(yt):
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

    which = str(input("Which resolution you want?")) +'p'

    try:
        print(list)
        index = list.index(which)
        res = list[index]
        print("The desired Resolution is:", res)
        return res

    except ValueError:
        print("Did nat find")


def GetPath():
    global path
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open the Windows Explorer dialog for selecting a folder
    path = filedialog.askdirectory()




def download_video(youtube_url):
    global path #path of download that user choice

    try:
        yt = YouTube(youtube_url)  #this gets the vide
        print("The Current video is:", yt.title)
        #confirmation()  #confirmation for download exits if user says no continues if yes

        resolution = GetResolutions(yt)

        #print with desired resolution


        video = yt.streams.filter(res=resolution).first()

        video.download(output_path=path) #this straight forward
        print("Video downloaded successfully.")

    except Exception as e:
        print(f"Error downloading video: {e}")



if __name__ == "__main__":
    intro() #goes through the intro first thing
    video_url = input("Enter the YouTube video link: ")
    download_video(video_url)