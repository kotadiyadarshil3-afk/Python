## Q1

print("Darsil","Kotadiya", sep="-")

print("Darshil", end=" ")
print("Kotadiya")

# print("======== Q2 =========")

# name = input("Enter your Name:")
# age = int(input("Enter your age:"))
# hobby = input("Enter your hooby:")

# print(f"Hello, {name}! At {age}, enjoying {hobby} sound fun!")

print("======== Q3 =======")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number: "))

print("====== Addition =======")
Add = num1 + num2
print("Addition", Add)

print("======== subtraction =======")
sub = num1 - num2
print("subtraction", sub)

print("========= multiplication =========")
mult = num1 * num2 
print("multiplication", mult)

print("========= division =========")
div = num1 / num2
print("division", div)

print("========= floor division ==========")
floor  = num1 // num2
print("floor division", floor)

print("========== Q4 ==========")

str = str("Darshil Koatdiya")
In = int(18)
floa = float(18.18)
bool = bool(True)

print("String:",str,type(str))
print("Interger:", int, type(int))
print("Float:",floa, type(floa))
print("Boolean:", bool, type(bool))

print("======= Q5 =======")

name = input("Enter your name:")
height = float(input("Enter your height:"))
Weight = float(input("Enter your Weight:"))

print(f"{name} your Height {height} and your weight is {Weight}")

print("======= Q6 =======")

a = input("Enter first boolean value (True/False):")
b = input("Enter secound boolean value (True/False):")

print("First value:",a)
print("Second value:",b)

print("\nUsing AND :", a and b )
print("Using OR :", a or b)
print("Using Not on first value:", not a)
print("Using Not on secound value:", not b)

print("======= Q7 =======")

num = int(input("Enter a number:"))
print("Original value =", num)

num += 5
print("After adding 5 =", num)

num -= 3
print("After -= 3:", num)

num *= 2
print("After *= 2:", num)

num /= 4
print("After /= 4:", num) 