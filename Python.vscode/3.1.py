print("================== Q1 ==================")

a = int(input("Enter a number to check that the number is odd or even:"))

if a % 2 == 0:
    print(f"{a} is Even")
else:
    print(f"{a} is Odd")

print()

print("=============== Q2 ==================")

age = int(input("Enter your age:"))

if age >= 0:
    if age <=12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior")

print()

print("================== Q3 ===================")

a = int(input("Enter your First number:"))
b = int(input("Enter your Second number:"))
c = int(input("Enter your Third number:"))

if a >= b and a >= c:
    print("Largest Number =",a)
elif b >= a and b >= c:
    print("Largest Number =",b)
else:
    print("Largest Number =",c)

print()

print("===================== Q4 ===================")

num = int(input("Enter a number:"))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Neutral Number")