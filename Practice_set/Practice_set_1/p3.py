name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
student = input("Are you a student? (yes/no): ").lower() == "yes"

print("Name:", name, "Age:", age, "Height:", height, "Student:", student)
print("Age:", age)
print("Height:", height)
print("Student:", student)

print(f"name: {name}", f"age: {age}", f"height: {height}", f"student: {student}")