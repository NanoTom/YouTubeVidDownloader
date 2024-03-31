from pytube import YouTube


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
    #print(f"{list}")

    which = str(input("Which one in the list you want lil bro?")) +'p'
    #print(which)

    # #method 1:
    # if which in list:
    #     print("int({which}) You choce this")
    # else:
    #     print("Error")

    #method 2

    #this will be implemented
    try:
        index = list.index(which)
        res = list[index]
        res = res[:-1]
        print(res)


    except ValueError:
        print("Did nat find")

if __name__ == "__main__":
    yt = YouTube("https://www.youtube.com/watch?v=8jTjNMkWOzM&list=PLM67FvWTFYwsLnknxoGen9nnRUuP2PaJP&index=11&ab_channel=Audioandlyrics")
    GetResolutions(yt)