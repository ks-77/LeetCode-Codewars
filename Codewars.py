# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# Given a string of digits, you should replace any digit below 5 with '0'
# and any digit 5 and above with '1'. Return the resulting string.


def fake_bin(x):
    result = ""
    for num in x:
        digit = int(num)
        if digit < 5:
            result += '0'
        else:
            result += '1'
    return result


# The goal of this exercise is to convert a string to a new string where each character in the new string is "("
# if that character appears only once in the original string,
# or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.


def duplicate_encode(word):
    result = ''
    word = word.lower()
    for char in word:
        count = word.count(char)
        if count > 1:
            result += ')'
        else:
            result += '('
    return result


# Create a function that returns the sum of the two lowest positive numbers given an array of positive integers.
# No floats or non-positive integers will be passed.


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0. Your function only needs to return the result,
# what is shown between parentheses in the example below is how you reach that result, and it's not part of it,
# see the sample tests.
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)


def summation(num):
    return sum(range(1, num + 1))


# This code does not execute properly. Try to figure out why.
# def multiply(a, b):
#     a * b


def multiply(a, b):
    return a * b


# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


def xo(string):
    count_x = string.lower().count('x')
    count_o = string.lower().count('o')

    return count_x == count_o


# Write a function called sumIntervals/sum_intervals that accepts an array of intervals,
# and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.


def sum_of_intervals(intervals):
    intervals.sort()
    sum = 0
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            sum += current_end - current_start
            current_start, current_end = start, end

    sum += current_end - current_start
    return sum