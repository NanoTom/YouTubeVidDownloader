class Vechile():
    def __init__(self, bodystyle):  #wht is mean self
        #the reference to the object is always the first parameter it can be nammed anyhing
        self.bodystyle = bodystyle

    def drive(self,speed):
        self.mode = "driving"
        self.speed = speed


class car(Vechile):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self,speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

class Motor(Vechile):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)


car1 = car("Gas type")
car2 = car("Electrical")
mc1 = Motor("gas",False)

print("Car 1 has" +str(car1.wheels)+" "+ str(car2.wheels))
print("alo" +str(mc1.bodystyle))

car1.drive(30)
car2.drive(40)
mc1.drive(50)

## make different type of cars