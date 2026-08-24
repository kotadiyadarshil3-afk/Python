# print("==================== Q1 =====================")

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))

# if a > b:
#     if a > c:
#         print("Maximum Number =", a)
#     else:
#         print("Maximum Number =", c)
# else:
#     if b > c:
#          print("Maximum Number =", b)
#     else:
#          print("Maximum Number =", c)

# print()

# print("================= Q2 ======================")

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))

# if a < b:
#     if a < c:
#         print("Minimum Number =", a)
#     else:
#         print("Minimum Number =", c)
# else:
#     if b < c:
#          print("Minimum Number =", b)
#     else:
#          print("Minimum Number =", c)

# print()

# print("================= Q3 =================")

# a = int(input("Enter First Number: "))
# b = int(input("Enter Secound Number: "))
# c = int(input("Enter Third Number: "))
# d = int(input("Enter Fourth Number: "))

# if a > b:
#     if a > c:
#         if a > d:
#             print("Maximum Number =", a)
#         else:
#             print("Maximum Number =", d)
#     else:
#         if c > d:
#             print("Maximum Number =", c)
#         else:
#             print("Maximum Number =", d)
# else:
#     if b > c:
#         if b > d:
#             print("Maximum Number =", b)
#         else:
#             print("Maximum Number =", d)
#     else:
#         if c > d:
#             print("Maximum Number =", c) 
#         else:
#             print("Maximum Number =", d)

# print()

# print("============= Q4 ===============")

# opt = input("Enter the Operator (+, -, /, *):")

# a = float(input("Enter First Number:"))
# b = float(input("Enter second Number:"))

# match opt:

#     case "+":
#         print("Result =", a + b)

#     case "-":
#         print("Result =", a - b)

#     case "/":
#         print("Result =", a / b)

#     case "*":
#         print("Result =", a * b)

#     case _:
#         print("Invalid Operator")

# print()

# print("============= Q5 =============")

# print("===== FAST FOOD MENU ====")
# print("1. Sandwich")
# print("2. Pizza")
# print("3. Burger")

# choice = int(input("Enter Your Choice: "))

# match choice:
#     case 1:
#         print("\n--- Sandwich Menu ---")
#         print("1. Veg Sandwich")
#         print("2. Cheese Sandwich")
#         print("3. Grilled Sandwich")

#         sub_choice = int(input("Enter your Choice: "))

#         match sub_choice:

#             case 1:
#                 print("You ordered Veg Sandwich")
#             case 2:
#                 print("You ordered Cheese Sandwich")
#             case 3:
#                 print("You ordered Grilled sandwich")
#             case _:
#                 print("Invalid Sandwich choice")

#     case 2:
#         print("\n--- Pizza Menu ---")
#         print("1. Thin Crust Pizza")
#         print("2. Chesse Burst Pizza")
#         print("3. Fresh Dough Pizza")

#         sub_choice = int(input("Enter your choice: "))

#         match sub_choice:
#             case 1:
#                 print("You ordered Thin Crust Pizza")
#             case 2:
#                 print("You ordered Chesse Burst Pizza")
#             case 3:
#                 print("You ordered Fresh Diugh Pizza")
#             case _:
#                 print("Invalid Pizza choice")

#     case 3:
#         print("\n--- Burger Menu ---")
#         print("1. Veg Burger")
#         print("2. Cheese Burger")
#         print("3. Double patty Burger")

#         sub_choice = int(input("Enter your choice: "))

#         match sub_choice:
#             case 1:
#                 print("You Orderd Veg Burger")
#             case 2:
#                 print("You Orderd Chesse Burger")
#             case 3: 
#                 print("You Orderd Double patty Burger")
#             case _:
#                 print("Invalid Burger choice")

#     case _:
#         print("Invalid menu choice")


print("================= Q6 ================")

print("===== TELECOM CALLING SYSTEM =====")
print("1. English")
print("2. Hindi")
print("3. Gujarati")

choice = int(input("Enter your language choice:"))

match choice:

    case 1:
        print("\n--- English Menu ---")
        print("1. Customer Care")
        print("2. Recharege")
        print("3. Balance Check")

        sub_choice = int(input("Enter your choice: "))

        match sub_choice:
            case 1:
                print("Connecting to Customer care...")
            case 2:
                print("Recharege option selected")
            case 3:
                print("Balance Check Selected")
            case _:
                print("Invalid choice")

    case 2:
        print("\n--- Hindi Menu ---")
        print("1. Customer Care")
        print("2. Recharege")
        print("3. Balance Check")

        sub_choice = int(input("Enter your choice: "))

        match sub_choice:
            case 1:
                print("Customer Care se connect ho raha hai... ")
            case 2:
                print("Recharge option select kiya gaya")
            case 3:
                print("Balance Check option select kiya gaya")
            case _:
                print("Invalid choice")

    case 3:
        print("\n--- Gujarati Menu ---")
        print("1. Customer Care")
        print("2. Recharge")
        print("3. Balance Check")

        sub_choice = int(input("Enter your choice: "))

        match sub_choice:
            case 1:
                print("Customer Care sathe connect thai rahyu chhe...")
            case 2:
                print("Recharge option pasand karyo")
            case 3:
                print("Balance Check option pasand karyo")
            case _:
                print("Invalid choice")

    case _:
        print("Invalid language choice")