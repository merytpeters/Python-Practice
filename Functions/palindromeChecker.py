#!/usr/bin/env python3
"""Palindrome Checker, a palindrome is a word or number that is the
same backwards"""


def checkPalindrome(word):
    """Function that checks for a palindrome"""
    reversed_word = ''.join(reversed(word))
    if reversed_word == word:
        print(f"{reversed_word} is a palindrome.")
        return reversed_word
    print(f"{reversed_word} is not a palindrome.")
    return None


def main():
    word = input("Enter the word:")
    checkPalindrome(word)


if __name__ == "__main__":
    main()
