#Q1

def multiply(a, b):
    return a * b

A = int(input("Enter a number: "))
B = int(input("Enter a number: "))

result = multiply(A, B)   # ONE value returned, catch in ONE variable
print(result)

#Q2
def introduce(name, language="Python"):
    return f"Hi! My name is {name} and i know the languge {language} "

Name = input("Enter your name : ")
Language = input("Enter the language you know : ")
result = introduce(Name,Language)

print(result)

#Q3
def circle_info(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    return area,circumference

r= int(input("Enter Radius :"))
are , circ =circle_info(r)
print(f"Area of the circle is {are}")
print(f"Circumference of the circle is {circ}")

#Q4
def bill_summary(items, discount=0):
    original = sum(items)
    discounted = original * discount /100
    final = original - discounted
    return original ,final

items = list(map(int, input("Enter prices separated by space: ").split()))
dicount = int(input("Enter dicount percent: "))
original,final = bill_summary(items,dicount)
print(f"original total is {original}")
print(f"amount after discount is {final}")
