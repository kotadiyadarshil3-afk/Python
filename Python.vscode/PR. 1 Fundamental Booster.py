print("Welcome to the Interactive Person Data Collector!")

name = input("Please enter your name:")
age = int(input("Please enter your age:"))
height = float(input("Please enter your height in meters:"))
fav_num = int(input("Please enter your favorite number:"))

print("\nThank you! Here is the information you provided:")

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_num} (Type: {type(fav_num)}, Memory Address: {id(fav_num)})")

current_year = 2026
birth_year = current_year - age
print(f"Birth Year: {birth_year} (Type: {type(birth_year)}, Memory Address: {id(birth_year)})")

print("\nThank you for using the Personal Data Collector. Goodbye!")
