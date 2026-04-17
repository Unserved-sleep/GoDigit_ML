try:
    PI = 3.1415926
    radius = int(input("Enter the radius of the circle: "))
    area = PI*radius**2
    print(area)
    print(type(area))
except:
    print("Invalid input")