#Q1 find num >5
nums =[3,7,2,9,4]
lrg =[]
for x in nums:
    if x > 5:
        lrg.append(x)

print(lrg)        

#Q2 
name="nisarga"
age=23
disc="my name is nisarga im 23 years old"
print(disc)

#Q3

fruite=["apple","bananna","strawberry","chikoo"]
l=fruite[0]
f=fruite[-1]
print(l,f)

#Q4

fruit=["apple","bananna","strawberry","chikoo"]
fruit.append("mango")
print(fruit)

#Q5

num=[1,2,3,4,5,6,7,8,9,0]
num[1]=99
print(num)

#medium level

#Q1
marks = [85, 90, 78, 92, 88]
largest=max(marks)
smallest=min(marks)
print(largest,smallest)

#Q2
items = ["pen", "book", "eraser"]
items.remove("book")
print(items)

#Q3
a=5
b=10
a=a+b
b=a-b
a=a-b
print("a =",a,"b =",b)

#Q4
nums=[1,2,3,4,5]
sqr=[]
for x in nums:
      sqr.append(x*x)
print(sqr)
    
#Q5
words = ["hello", "world", "python"]
line=" " .join(words)
print(line)

#hard level
#Q1
shopping = ["milk", "eggs", "bread", "butter"]
for i in range(len(shopping)):
    print(i+1, ".", shopping[i])

#Q2

evens = [2, 4, 6]  
odds = [1, 3, 5]
joint=evens+odds
joint.sort()
print (joint)
