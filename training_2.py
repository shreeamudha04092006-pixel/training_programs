
# 1. Student Analysis

students = [
    ("Asha", 85, 78, 92),
    ("Bala", 65, 72, 70),
    ("Charan", 90, 88, 95),
    ("Divya", 76, 80, 74),
    ("Esha", 60, 68, 72)
]

qualified = []
highest = 0
topper = ""

for student in students:
    name = student[0]
    total = student[1] + student[2] + student[3]
    average = total / 3

    if average >= 75:
        qualified.append(name)

    if total > highest:
        highest = total
        topper = name

print("1. Student Analysis")
print("Qualified Students:", qualified)
print("Topper:", topper)


# 2. Remove Duplicates

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("\n2. Remove Duplicates")
print("Unique Numbers:", result)


# 3. Word Frequency

text = "python is easy and python is powerful"

words = text.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\n3. Word Frequency")
print("Word Frequency:", frequency)


# 4. Square of Marks

marks = [45, 82, 67, 91, 76, 55, 88]

result = []

for mark in marks:
    if mark >= 70:
        result.append(mark ** 2)

print("\n4. Square of Marks")
print("Squared Marks:", result)


# 5. Two Sum

numbers = [2, 7, 11, 15]
target = 9

print("\n5. Two Sum")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Target Pair Index:", [i, j])


# 6. Anagram Check

word1 = "listen"
word2 = "silent"

print("\n6. Anagram Check")

if sorted(word1) == sorted(word2):
    print("Anagram: True")
else:
    print("Anagram: False")


# 7. Duplicate Check

numbers = [1, 2, 3, 1]

print("\n7. Duplicate Check")

if len(numbers) != len(set(numbers)):
    print("Duplicate Found: True")
else:
    print("Duplicate Found: False")


# 8. Largest Number

numbers = [10, 25, 15, 40, 30]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("\n8. Largest Number")
print("Largest Number:", largest)


# 9. Sum and Average

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

average = total / len(numbers)

print("\n9. Sum and Average")
print("Total:", total)
print("Average:", average)


# 10. Unique Characters

text = "aabbcdde"

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("\n10. Unique Characters")

for character in frequency:
    if frequency[character] == 1:
        print("Unique Character:", character)

