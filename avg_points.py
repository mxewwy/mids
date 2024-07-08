from numpy.random import normal
import time

amount = int(input("Enter an amount of marks: "))
start = time.time()
marks = {}
with open("gradepoints.txt", encoding="UTF-8") as file:
    for stud in file:
        key, value = stud.strip("\n").split(":")
        marks[key] = float(value)
for stud in marks:
    midsum = 0
    print(f"Academic report - {stud}.")
    norm = normal(size=amount)
    for i in range(amount):
        mark = round(marks[stud] + int(norm[i]))
        if mark > 5:
            mark = 5
        if mark < 2:
            mark = 2
        midsum += mark
        print(f"{i+1} - {mark}")
    print(f"Average grade point of student - {midsum/amount}.")
end = time.time()
print(f"A report was generated for {end-start} seconds.") 

