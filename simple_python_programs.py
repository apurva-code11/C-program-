1.
print("Hello, World!")

2.
num1 = 5
num2 = 10
print(num1 + num2)

3.
num = float(input())
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

4.
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

5.
a = 5
b = 10
a, b = b, a
print(a, b)

6.
celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

7.
import random
print(random.randint(1, 100))

8.
kilometers = float(input())
miles = kilometers * 0.621371
print(miles)

9.
for i in range(1, 11):
    print(i)

10.
num = int(input())
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

11.
numbers = [4, 2, 9, 7, 5]
print(max(numbers))

12.
numbers = [4, 2, 9, 7, 5]
print(min(numbers))

13.
text = input()
print(text[::-1])

14.
num = int(input())
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)

15.
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

16.
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

17.
text = input()
print(len(text))

18.
text = input()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

19.
base = float(input())
height = float(input())
area = 0.5 * base * height
print(area)

20.
numbers = [1, 2, 3, 4, 5]
print(sum(numbers) / len(numbers))