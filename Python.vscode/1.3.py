print("======= Q1 =======")

value = input("Enter a value:")

print("Original value:", value)
print("Origibal value type:", type(value))

print("\nInterger value:", int(value), type(int(value)))
print("Float value:", float(value), type(float(value)))
print("Boolen value:", bool(value), type(bool(value)))
print()

print("======= Q2 =======")

num = float(input("Enter a number with decimal point:"))

print("Float number:", num)
print("Integer number:", int(num))
print()

print("======= Q3 =======")
value = input("Enter the value in True or False: ") == "True" 

print("Boolen Value:", value)
print("Integer value:", int(value))
print("String value:", str(value))
print()

print("======= Q4 =======")

a = 10
b = 10.2
c = "Darshil"
d = True
e =[1,2,3]
f =(1,2,3)
g ={"Name":"Darshil"}

print("Integer:", a, type(a), id(a))
print("Float:", b, type(b), id(b))
print("String:", c, type(c), id(c))
print("Boolean:", d, type(d), id(d))
print("List:", e, type(e), id(e))
print("Tuple:", f, type(f), id(f))
print("Dictionary:", g, type(g), id(g))
print()

print("======= Q5 =======")

a = 100
b = 100

print("Before Changing")
print("a =", a, "Address of a:", id(a))
print("b =", b, "Address of b:", id(b))

b = 200
print("After changing")
print("a =", a, "Address of a:", id(a))
print("b =", b, "Address of b:", id(b))