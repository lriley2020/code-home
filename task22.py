import json
from math import pi

class Shape:
    @staticmethod
    def validate(measurements):
        for measurement in measurements:
            if not measurement.isnumeric():
                raise Exception("Measurements must be numbers")

class Rectangle(Shape):
    def showarea(self):
        return self.width * self.length

    def __init__(self, *measurements):
        self.validate(measurements)
        self.width, self.length = map(int, measurements)

class Cuboid(Shape):
    def showvolume(self):
        return self.width * self.length * self.height

    def __init__(self, *measurements):
        self.validate(measurements)
        self.width, self.length, self.height = map(int, measurements)

class Circle(Shape):
    def showarea(self):
        return pi * self.radius ** 2

    def __init__(self, *measurements):
        self.validate(measurements)
        self.radius, = map(int, measurements)

def jsonderulo(newshape):
    with open("shapes.json", "r+") as shapes:
        results = json.load(shapes)
        results.append(newshape)
        shapes.seek(0)
        json.dump(results, shapes)


options = ["Area of rectangle", "Volume of cuboid", "Area of circle", "See previous calculations", "Quit"]
for i in range(len(options)): print(f"{i + 1}) {options[i]}")
option = int(input("option> "))
match option:
    case 1:
        myrectangle = Rectangle(input("width> "), input("length> "))
        result = myrectangle.showarea()
        print(f"The area is {result}cm²")
        jsonderulo(("rectangle", result))
    case 2:
        mycubiod = Cuboid(input("width> "), input("length> "), input("height> "))
        result = mycubiod.showvolume()
        print(f"The volume is {result}cm³")
        jsonderulo(("rectangle", result))
    case 3:
        mycircle = Circle(input("radius> "))
        result = mycircle.showarea()
        print(f"The area is {result}cm²")
        jsonderulo(("circle", result))
    case 4:
        with open("shapes.json", "r") as shapes:
            for shape in json.load(shapes): print(*shape)
    case 5:
        raise SystemExit
