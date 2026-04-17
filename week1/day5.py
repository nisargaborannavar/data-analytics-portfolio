#conditional statements
#Q1
score=int(input("Enter you score : "))
if score >= 90:
    print("Grade: A") 
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else: 
    print("Grade: F")

#Q2
year = int(input("Enter year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else:
    print("It's not a leap year")

#Q3
username="liashook"
password=2444
enter=input("enter user name :")
penter=int(input("enter paswrod:"))
if enter==username and penter==password:
    print("Access Granted")
elif enter==username and penter!=password:
    print("Wrong password!")
elif enter!=username and penter==password:
    print("invalid username")

#functions
#Q1
def bmi(weight, height, unit="metric"):
    if unit == "metric":
        BMI = weight / (height * height)
    else:
        BMI = 703 * weight / (height * height)

    if BMI < 18.5:
        category = "Underweight"
    elif BMI < 25:
        category = "Normal"
    elif BMI < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return BMI, category
   
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
unit = input("Enter unit (metric/imperial): ").strip().lower()
result, category = bmi(weight, height, unit)
print(f"BMI: {result:.2f} — {category}")

#Q2
def convert(temp, to="F"):
    if to == "C":
        value = (temp - 32) * 5/9
        label = f"{value} °C"
    elif to == "K":
        value = temp + 273.15
        label = f"{value} K"
    else:
        value = temp
        label = f"{value} °F"

    return value, label
temp = float(input("Enter tempararue: "))
to = input("Enter Temprature value").strip().upper() 
value, label = convert(temp, to)
print(label)

#Q3
def solve(li):
   
    min_val = min(li)
    max_val = max(li)
    mean=sum(li)/len(li) 
    count=len(li)  
    
    return min_val,max_val,mean,count
user_input = input("Enter numbers separated by space: ")
nums = user_input.split()   # ['5', '89', '23', ...]

nums = [int(n) for n in nums]   # convert to integers
min_val, max_val, mean, count = solve(nums)
print(f"min={min_val}, max={max_val}, mean={mean:.2f}, count={count}")

#String format
#Q1
grreting = input("Enter your full name: ")
result = grreting.strip().title()
print(result)

#Q2
