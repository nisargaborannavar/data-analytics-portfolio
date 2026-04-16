for i in range(2):
    for j in range(3):
        print(i,j)

products = ["milk", "bread", "butter"]
prices = [50, 30, 60]
for products, price in zip(products, prices):
    print(products, price)
#dictonary

#Q1
student = {
    "Name" : "Nisarga",
    "Age" : 23,
    "Grade" : "A"

}
print(student)

#Q2
person = {"name": "Arjun", "age": 20}
person["city"]="sangli"
person["age"] = 23
print(person)

#Q3
user = {"name": "Priya", "phone": "9876543210"}
if "email" in user:
    print("Found")
else:
    print("Not found")

#Q4
info = {"name": "Rahul", "age": 22, "city": "Pune"}
info.pop("age")
print(info)

#looP
#Q1
for i in range(1,11):
    print(i)

#Q2

for i in range(1,21):
    if i%2==0:
        print(i)

#Q3

sum=0
for i in range(1,101):
    sum=sum+i
print("sum",sum)

#Q4

marks = {"Maths": 95, "Science": 88, "English": 76}
for key in marks:
    print(key,marks[key])

#Q5
marks = {"Maths": 95, "Science": 78, "English": 85, "Hindi": 60}
for subject, score in marks.items():
    if score > 80:
        print(subject, score)

#Q6
names = ["Aman", "Priya", "Rahul", "Sneha"]
name_lengths = {}
for name in names:
    name_lengths[name] = len(name)
print(name_lengths)