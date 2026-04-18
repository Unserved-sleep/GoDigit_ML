class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height} feet"

jhon = Person("Jhon", 25, 5.84)
print(f"Person Details: {jhon}", end="\n\n")

print(f"Person Details with Expression: {jhon.name.upper()}, {jhon.age + 5}, {jhon.height:.1f} feet", end="\n\n")

print(f"People Details Multi-line:\n"
      f"Name: {jhon.name}\n"
      f"Age: {jhon.age}\n"
      f"Height: {jhon.height:.2f} feet", end="\n\n")

print("-"*40)
print(f"| {'Name':<10} | {'Age':^10} | {'Height':>10} |")
print("-"*40)
print(f"| {jhon.name:<10} | {jhon.age:^10} | {jhon.height:>10} |")
print("-"*40, end="\n\n")

template_string = ("Hello, {name}!\n"
                   "Your age is {age} years old.\n"
                   "You are {height} feet tall.\n")
formatted_string = template_string.format(name=jhon.name, age=jhon.age, height=jhon.height)
print(formatted_string)