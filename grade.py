name = input("Enter student name: ")
mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))

average = (mark1 + mark2) / 2
total = mark1 + mark2
print("\nStudent Name:", name)
print("Average Mark:", average)
print("Total Mark:", total)
if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

