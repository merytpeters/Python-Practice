#!/usr/bin/env python3
"""Reversing strings in python"""


def strReversal(original_str):
    """First method using slicing"""
    reversed_string = original_str[::-1]
    return reversed_string


def stringReversed(original_str):
    """Second method using join and reversed"""
    reversed_str = ''.join(reversed(original_str))
    return reversed_str


def strReversed(original_string):
    """Third method using loop"""
    reversed_string = ''
    for char in original_string:
        reversed_string = char + reversed_string
    return reversed_string


def main():
    word1 = input("Enter the first word:")
    reversed1 = strReversed(word1)
    print(f"method 1: {reversed1}")
    word2 = input("Enter the second word:")
    reversed2 = stringReversed(word2)
    print(f"method 2: {reversed2}")
    word3 = input("Enter the third word:")
    reversed3 = strReversal(word3)
    print(f"method 3: {reversed3}")


if __name__ == "__main__":
    main()
