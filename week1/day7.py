#Q1


#Q5
with open("week1/numbers.txt","r") as f:
    lines = f.readlines()
    total = 0

    for line in lines:
     total += int(line)

print(total)
