print("================= Q1 ================")

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break 

    print("You entered:", num)

print()

print("================ Q2 =================")

for i in range(1,11):
    print("Square of", i, "=", i ** 2)

print()

print("=============== Q3 ==================")

num = 1

while num <= 50:
    if num % 2 == 0:
        print(num)

    num += 1

print()

print("=============== Q4 ===================")

for num in range(1,21):
    if num % 2 != 0:
        print(num)

print()

print("=============== Q5 ==================")

for num in range(5,51,5):
    print(num)
print()

print("============== Q6 ===================")

for num in range(10, 0, -1):
    print(num)

print()

print("============= Q7 =================")

for num in range(1,51):

    if num % 2 == 0 and num % 3 == 0:
        print(num, "- Divisible by both")
    elif num % 2 == 0:
        print(num, "- Divisible by 2")
    elif num % 3 == 0:
        print(num, "- Divisible by 3")