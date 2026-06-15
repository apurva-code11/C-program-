# ==========================================================
# MASTER PYTHON FILE: 20 BASIC TO INTERMEDIATE UTILITY SCRIPTS
# ==========================================================

# ============================================================
# START OF FILE: 01_hello_world.py
# ============================================================

# Program 01: Hello World
# The foundational program demonstrating basic text output and input.

def main():
    print("Hello, Python World!")
    user_name = input("Please enter your name: ")
    print(f"Welcome to Python programming, {user_name}!")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 02_odd_even.py
# ============================================================

# Program 02: Odd or Even Checker
# Demonstrates conditional branching (if-else) and the modulo operator.

def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    print("--- Odd or Even Checker ---")
    try:
        num = int(input("Enter an integer: "))
        result = check_odd_even(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 03_simple_calculator.py
# ============================================================

# Program 03: Simple Calculator
# Implements basic arithmetic functions and choice-driven logic.

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

def main():
    print("--- Simple Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Select operation (1-4): ")
    
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1': print(f"Result: {add(num1, num2)}")
            elif choice == '2': print(f"Result: {subtract(num1, num2)}")
            elif choice == '3': print(f"Result: {multiply(num1, num2)}")
            elif choice == '4': print(f"Result: {divide(num1, num2)}")
        except ValueError:
            print("Invalid number input.")
    else:
        print("Invalid operational choice.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 04_find_largest.py
# ============================================================

# Program 04: Find Largest of Three Numbers
# Demonstrates logical operators (and, or) within conditionals.

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    print("--- Find the Largest Number ---")
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        z = float(input("Enter third number: "))
        largest = find_largest(x, y, z)
        print(f"The largest number among {x}, {y}, and {z} is {largest}.")
    except ValueError:
        print("Please enter numeric values.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 05_leap_year.py
# ============================================================

# Program 05: Leap Year Checker
# Implements multi-tiered condition testing for calendar leap years.

def is_leap_year(year):
    # A year is leap if divisible by 4, but not by 100 unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    print("--- Leap Year Checker ---")
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Please enter a valid year format.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 06_factorial.py
# ============================================================

# Program 06: Factorial of a Number
# Shows how to use loops to compute mathematical sequences.

def calculate_factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print("--- Factorial Calculator ---")
    try:
        num = int(input("Enter a positive integer: "))
        print(f"The factorial of {num} is {calculate_factorial(num)}.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 07_multiplication_table.py
# ============================================================

# Program 07: Multiplication Table Generator
# Demonstrates basic 'for' loop ranges and structured formatting output.

def main():
    print("--- Multiplication Table Generator ---")
    try:
        num = int(input("Enter the number for the table: "))
        limit = int(input("Enter the table range limit (e.g., 10): "))
        
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, limit + 1):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 08_fibonacci.py
# ============================================================

# Program 08: Fibonacci Sequence Generator
# Implements iterative array handling to output sequences.

def generate_fibonacci(terms):
    if terms <= 0: return []
    if terms == 1: return [0]
    
    seq = [0, 1]
    while len(seq) < terms:
        seq.append(seq[-1] + seq[-2])
    return seq

def main():
    print("--- Fibonacci Sequence ---")
    try:
        count = int(input("How many terms do you want to generate? "))
        print(f"Sequence: {generate_fibonacci(count)}")
    except ValueError:
        print("Please enter an integer.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 09_prime_check.py
# ============================================================

# Program 09: Prime Number Checker
# Evaluates integers using division loops to verify prime statuses.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("--- Prime Number Verification ---")
    try:
        num = int(input("Enter an integer to test: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is a composite/non-prime number.")
    except ValueError:
        print("Please enter a clean integer.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 10_palindrome_string.py
# ============================================================

# Program 10: String Palindrome Checker
# Tests if a word reads identically forwards and backwards using slices.

def is_palindrome(text):
    clean_text = "".join(ch.lower() for ch in text if ch.isalnum())
    return clean_text == clean_text[::-1]

def main():
    print("--- Palindrome Checker ---")
    user_string = input("Enter a word or phrase: ")
    if is_palindrome(user_string):
        print("Yes, it is a palindrome!")
    else:
        print("No, it is not a palindrome.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 11_count_vowels.py
# ============================================================

# Program 11: Count Vowels in a String
# Uses sets and iteration loop structures to extract structural content counts.

def count_vowels(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def main():
    print("--- Vowel Counter ---")
    phrase = input("Enter a sentence: ")
    print(f"Number of vowels found: {count_vowels(phrase)}")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 12_list_average.py
# ============================================================

# Program 12: Calculate Average of a List
# Demonstrates collection manipulation (lists) along with sum() and len().

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print("--- List Average Calculator ---")
    # Statically defined array list as a showcase template
    sample_list = [45, 12, 89, 34, 67, 90, 21]
    print(f"Target List: {sample_list}")
    print(f"Calculated Arithmetic Mean / Average: {calculate_average(sample_list):.2f}")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 13_reverse_string.py
# ============================================================

# Program 13: Reverse a String
# Demonstrates direct core slicing and traditional loop methods to invert data profiles.

def reverse_with_slice(s):
    return s[::-1]

def reverse_with_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    print("--- String Reversal ---")
    text = input("Enter a string to invert: ")
    print(f"Reversed via slicing: {reverse_with_slice(text)}")
    print(f"Reversed via loop method: {reverse_with_loop(text)}")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 14_dictionary_squares.py
# ============================================================

# Program 14: Generate Squares Dictionary
# Explores key-value maps (dictionaries) built natively via loops.

def generate_squares_dict(limit):
    squares_dict = {}
    for i in range(1, limit + 1):
        squares_dict[i] = i * i
    return squares_dict

def main():
    print("--- Squares Dictionary ---")
    try:
        n = int(input("Enter maximum integer boundary: "))
        result = generate_squares_dict(n)
        print("Generated Key-Value Mapping (Number -> Square):")
        print(result)
    except ValueError:
        print("Invalid limit entry.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 15_file_writer_reader.py
# ============================================================

# Program 15: Text File Input/Output
# Uses safe Python context blocks to create, append, and access external documents.

def main():
    filename = "demo_log.txt"
    
    print(f"Writing static headers onto {filename}...")
    with open(filename, "w") as file:
        file.write("Python File I/O Demonstration Header.\n")
        file.write("Line 02: Storing raw string arrays directly.\n")
        
    print(f"Reading back generated lines from {filename}:\n")
    with open(filename, "r") as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 16_celcius_fahrenheit.py
# ============================================================

# Program 16: Celsius and Fahrenheit Converter
# Handles mathematical equations for bidirectional physical units.

def c_to_f(celsius): return (celsius * 9/5) + 32
def f_to_c(fahrenheit): return (fahrenheit - 32) * 5/9

def main():
    print("--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
    mode = input("Choose direction (1 or 2): ")
    
    try:
        val = float(input("Enter temperature value to convert: "))
        if mode == '1':
            print(f"{val}°C is equivalent to {c_to_f(val):.2f}°F")
        elif mode == '2':
            print(f"{val}°F is equivalent to {f_to_c(val):.2f}°C")
        else:
            print("Invalid conversion choice.")
    except ValueError:
        print("Input standard real numbers only.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 17_guess_number_game.py
# ============================================================

# Program 17: Interactive Number Guessing Game
# Integrates pseudorandom loops matching user responses to hidden targets.
import random

def main():
    print("--- Guess the Hidden Number ---")
    target = random.randint(1, 50)
    attempts = 0
    print("I have selected a hidden integer between 1 and 50.")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < target:
                print("Too low! Try a higher number.")
            elif guess > target:
                print("Too high! Try a lower number.")
            else:
                print(f"Bingo! You discovered the target in {attempts} total attempts!")
                break
        except ValueError:
            print("Invalid guess entry. Input integers only.")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 18_find_min_max.py
# ============================================================

# Program 18: Find Min and Max in an Array
# Recreates standard min/max logic without relying on built-in methods.

def find_min_max(elements):
    if not elements:
        return None, None
    
    minimum = maximum = elements[0]
    for item in elements:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    return minimum, maximum

def main():
    print("--- Custom Min/Max Search ---")
    dataset = [23, 5, 87, 12, 64, -3, 42, 9]
    print(f"Target Collection: {dataset}")
    
    minimum, maximum = find_min_max(dataset)
    print(f"Minimum Element discovered: {minimum}")
    print(f"Maximum Element discovered: {maximum}")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 19_list_comprehension.py
# ============================================================

# Program 19: List Comprehension Demonstrations
# Shows how to construct and filter sequences in a single, readable line.

def main():
    print("--- List Comprehension Features ---")
    base_numbers = list(range(1, 11))
    print(f"Base Array List: {base_numbers}")
    
    # Generate squares using list comprehension
    squares = [x ** 2 for x in base_numbers]
    print(f"Transformed (Squares): {squares}")
    
    # Filter out odd numbers
    even_numbers = [x for x in base_numbers if x % 2 == 0]
    print(f"Filtered (Evens Only): {even_numbers}")

if __name__ == "__main__":
    main()


# ============================================================
# START OF FILE: 20_oop_concept.py
# ============================================================

# Program 20: Core Object-Oriented Blueprint
# Illustrates fundamental OOP principles: Classes, Methods, and Attributes.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def display_details(self):
        return f"Student Info -> Name: {self.name} | Age: {self.age} | Course Track: {self.course}"

def main():
    print("--- Simple Object-Oriented Programming (OOP) ---")
    # Instantiating student objects from our blueprint class
    student1 = Student("Emma Watson", 20, "Computer Science")
    student2 = Student("Liam Neeson", 22, "Data Analytics")
    
    print(student1.display_details())
    print(student2.display_details())

if __name__ == "__main__":
    main()


