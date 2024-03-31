import fileinput

def alo():
    file = open("Alo.txt","r")

    if (file.mode == "r"):
        f1 = file.readline()
        print(len(f1))
        print(f1)
        for i in f1:
            print(f1)

    file.close()

alo()
