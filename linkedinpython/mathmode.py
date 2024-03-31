import math


print("The square of 16 is", math.sqrt(16))

#exeption handling da shnu

try:
    #tr
        x = 10/0
    #exc
        print("Well that not good")
except SyntaxError as e:  #idk how to catch syntax errors need to learn this part
    print("gg")
except ZeroDivisionError as e:
    print("gandu" , e)
finally:
    print("This will always run")

print("pi is" ,math.pi)