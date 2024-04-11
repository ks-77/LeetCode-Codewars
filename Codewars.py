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