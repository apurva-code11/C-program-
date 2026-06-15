def is_armstrong(n):
    s = str(n)
    l = len(s)
    return sum(int(c) ** l for c in s) == n

def prime_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def is_perfect(n):
    if n <= 1:
        return False
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s == n

def single_digit_sum(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def is_num_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_compare(n):
    rev = int(str(n)[::-1])
    return rev == n

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b) if a and b else 0

def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

def is_prime_func(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def count_characters(s):
    vowels = "aeiouAEIOU"
    v_cnt = c_cnt = d_cnt = s_cnt = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_cnt += 1
            else:
                c_cnt += 1
        elif char.isdigit():
            d_cnt += 1
        else:
            s_cnt += 1
    return v_cnt, c_cnt, d_cnt, s_cnt

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def reverse_string_manual(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

def print_number_pattern(rows=5):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def is_str_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def second_largest(lst):
    if len(lst) < 2:
        return None
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

def remove_duplicates_manual(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def element_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

def merge_and_sort_manual(lst1, lst2):
    merged = lst1 + lst2
    n = len(merged)
    for i in range(n):
        for j in range(0, n - i - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
    return merged

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_list_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

def handle_exceptions():
    try:
        a = int(input())
        b = int(input())
        print(a / b)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
    except Exception:
        print("GeneralError")

import math
def math_module_demonstration(n):
    sqrt_val = math.sqrt(n) if n >= 0 else None
    fact_val = math.factorial(int(n)) if n >= 0 and float(n).is_integer() else None
    pow_val = math.pow(n, 2)
    return sqrt_val, fact_val, pow_val
