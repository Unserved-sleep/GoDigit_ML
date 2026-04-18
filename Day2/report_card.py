#New School of Learning
#3 name
#Physics, Chem, Maths
from typing import Final
school_name: Final = "New School Of Learning"
student1_name: str = input("Enter Student Name: ")
phy_marks, chem_marks, maths_marks = map(int,input(f"Enter Marks for {student1_name}: ").split())
per_phy_marks = phy_marks*2
per_chem_marks = chem_marks*2
per_maths_marks = maths_marks*2

print(f"{school_name} - Class XI - {student1_name}")
print("-"*73)
print(f"| {'Subject':^15} | {'Total Marks':^15} | {'Marks Obtained':^15} | {'Percentage':^15} |")
print("-"*73)
print(f"| {'Physics':^15} | {50:^15} | {phy_marks:^15} | {per_phy_marks:^15} |")
print(f"| {'Chemistry':^15} | {50:^15} | {chem_marks:^15} | {per_chem_marks:^15} |")
print(f"| {'Mathematics':^15} | {50:^15} | {maths_marks:^15} | {per_maths_marks:^15} |")
print("-"*73)
print(f"| {'Total':^15} | {150:^15} | {phy_marks+chem_marks+maths_marks:^15} | {(per_phy_marks+per_chem_marks+per_maths_marks)/3:^15} |")
print("-"*73)

student2_name: str = input("Enter Student Name: ")
phy_marks2, chem_marks2, maths_marks2 = map(int, input(f"Enter Marks for {student2_name}: ").split())
per_phy_marks2 = phy_marks2*2
per_chem_marks2 = chem_marks2*2
per_maths_marks2 = maths_marks2*2

print(f"{school_name} - Class XI - {student2_name}")
print("-"*73)
print(f"| {'Subject':^15} | {'Total Marks':^15} | {'Marks Obtained':^15} | {'Percentage':^15} |")
print("-"*73)
print(f"| {'Physics':^15} | {50:^15} | {phy_marks2:^15} | {per_phy_marks2:^15} |")
print(f"| {'Chemistry':^15} | {50:^15} | {chem_marks2:^15} | {per_chem_marks2:^15} |")
print(f"| {'Mathematics':^15} | {50:^15} | {maths_marks2:^15} | {per_maths_marks2:^15} |")
print("-"*73)
print(f"| {'Total':^15} | {150:^15} | {phy_marks2+chem_marks2+maths_marks2:^15} | {(per_phy_marks2+per_chem_marks2+per_maths_marks2)/3:^15} |")
print("-"*73)

student3_name: str = input("Enter Student Name: ")
phy_marks3, chem_marks3, maths_marks3 = map(int, input(f"Enter Marks for {student3_name}: ").split())
per_phy_marks3 = phy_marks3*2
per_chem_marks3 = chem_marks3*2
per_maths_marks3 = maths_marks3*2

print(f"{school_name} - Class XI - {student3_name}")
print("-"*73)
print(f"| {'Subject':^15} | {'Total Marks':^15} | {'Marks Obtained':^15} | {'Percentage':^15} |")
print("-"*73)
print(f"| {'Physics':^15} | {50:^15} | {phy_marks3:^15} | {per_phy_marks3:^15} |")
print(f"| {'Chemistry':^15} | {50:^15} | {chem_marks3:^15} | {per_chem_marks:^15} |")
print(f"| {'Mathematics':^15} | {50:^15} | {maths_marks3:^15} | {per_maths_marks3:^15} |")
print("-"*73)
print(f"| {'Total':^15} | {150:^15} | {phy_marks3+chem_marks3+maths_marks3:^15} | {(per_phy_marks3+per_chem_marks3+per_maths_marks3)/3:^15} |")
print("-"*73)

phy_total = phy_marks + phy_marks2 + phy_marks3
chem_total = chem_marks + chem_marks2 + chem_marks3
maths_total = maths_marks + maths_marks2 + maths_marks3

phy_average = phy_total/3
chem_average = chem_total/3
maths_average = maths_total/3

phy_class_avg = phy_average/3*2
chem_class_avg = chem_average/3*2
maths_class_avg = maths_average/3*2

total_marks = phy_total + chem_total + maths_total

overall_percent = (phy_class_avg + chem_class_avg + maths_class_avg)/3

print("Class Average and Percentage for Each Subject:")
print(f"Physics Average is {phy_class_avg:.2f} and Percentage is {phy_class_avg*2:.2f}%")
print(f"Chemistry Average is {chem_class_avg:.2f} and Percentage is {chem_class_avg*2:.2f}%")
print(f"Mathematics Average is {maths_class_avg:.2f} and Percentage is {maths_class_avg*2:.2f}%")
print(f"Overall Percentage is {overall_percent:.2f}%")





