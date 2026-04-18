

#Q3
def circle_info(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    return area,circumference

r= int(input("Enter Radius :"))
result=circle_info(r)
print (result)