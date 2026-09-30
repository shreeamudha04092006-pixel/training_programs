print("\n--- 1. Celsius to Fahrenheit ---")

c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print("Temperature in Fahrenheit:", f"{f:.2f}")


print("\n--- 2. Employee Salary ---")

basic = float(input("Enter basic salary: "))
hra = basic * 20 / 100
da = basic * 15 / 100
pf = basic * 8 / 100
net_salary = basic + hra + da - pf

print("HRA:", hra)
print("DA:", da)
print("PF:", pf)
print("Net Take-Home Salary:", net_salary)


print("\n--- 3. Leap Year ---")

year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


print("\n--- 4. Marks and Grade ---")

mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

average = (mark1 + mark2 + mark3) / 3

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 50:
    grade = "B"
else:
    grade = "Fail"

print("Average:", average)
print("Grade:", grade)


print("\n--- 5. Voting and Senior Citizen Discount ---")

age = int(input("Enter age: "))

voting = "Eligible to vote" if age >= 18 else "Not eligible to vote"
discount = "Senior citizen discount applicable" if age >= 60 else "No senior citizen discount"

print(voting)
print(discount)


print("\n--- 6. Multiplication Table ---")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


print("\n--- 7. Sum and Average ---")

n = int(input("Enter N: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

average = total / n

print("Sum:", total)
print("Average:", average)


print("\n--- 8. Prime Number ---")

n = int(input("Enter a number: "))

if n < 2:
    print("Not a Prime Number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")


print("\n--- 9. Reverse and Palindrome ---")

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse:", reverse)

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


print("\n--- 10. HTTP Status Code ---")

code = int(input("Enter HTTP status code: "))

match code:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status Code")