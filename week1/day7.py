# Q1 - open and read entire file
with open("week1/poem.txt", "r") as f:
    content = f.read()
print(content)

# Q2 - readlines() and print first 3
with open("week1/fruits.txt", "r") as f:
    lines = f.readlines()
print(lines[:3])

# Q3 - with open() rewrite
with open("data.txt", "r") as f:
    content = f.read()

# Q4 - count characters
with open("week1/poem.txt", "r") as f:
    content = f.read()
print(len(content))

# Q5 - sum numbers from file
with open("week1/numbers.txt", "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    total += int(line.strip())
print(total)

# Q6 - manual CSV, print each row as list
with open("week1/students.csv", "r") as f:
    for line in f:
        row = line.strip().split(",")
        print(row)

# Q7 - extract second column, skip header
with open("week1/products.csv", "r") as f:
    lines = f.readlines()

for line in lines[1:]:
    data = line.strip().split(",")
    print(data[1])

# Q8 - filter ERROR lines into new file
with open("log.txt", "r") as f:
    lines = f.readlines()

with open("errors.txt", "w") as f:
    for line in lines:
        if "ERROR" in line:
            f.write(line)

# Q9 - readline() in while loop, stop at empty line
with open("week1/poem.txt", "r") as f:
    while True:
        line = f.readline()
        if line == "" or line == "\n":
            break
        print(line.strip())

# Q10 - manual inspect then pandas
with open("week1/sales.csv", "r") as f:
    lines = f.readlines()
    for line in lines[:3]:
        print(line.strip().split(","))

import pandas as pd
df = pd.read_csv("week1/sales.csv")
print(df.head())

# Q11 - count rows manually, add row_index with pandas
with open("week1/employees.csv", "r") as f:
    lines = f.readlines()
print(f"Total rows (excluding header): {len(lines) - 1}")

import pandas as pd
df = pd.read_csv("week1/employees.csv")
df["row_index"] = range(1, len(df) + 1)
df.to_csv("employees_indexed.csv", index=False)

# Q12 - safe_read function with error handling
def safe_read(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: {filepath} not found.")
        return None

# Q13 - parse grades.csv, find average and top scorer
with open("week1/grades.csv", "r") as f:
    lines = f.readlines()

total = 0
highest = 0
top_student = ""

for line in lines[1:]:
    name, score = line.strip().split(",")
    score = int(score)
    total += score
    if score > highest:
        highest = score
        top_student = name

average = total / (len(lines) - 1)
print(f"Average score: {average:.2f}")
print(f"Top student: {top_student} with {highest}")

# Q14 - summarize log.txt into summary.txt
with open("log.txt", "r") as f:
    lines = f.readlines()

total_lines = len(lines)
blank_lines = sum(1 for line in lines if line.strip() == "")
hash_lines = sum(1 for line in lines if line.startswith("#"))

with open("summary.txt", "w") as f:
    f.write(f"Total lines: {total_lines}\n")
    f.write(f"Blank lines: {blank_lines}\n")
    f.write(f"Lines starting with #: {hash_lines}\n")