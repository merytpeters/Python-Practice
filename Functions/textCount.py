#!/usr/bin/env python3
"""Counts the frequency of character in a text"""


def textFrequency(word):
    """Text frequency function"""
    text_dict = {}
    char_count = 0
    for char in word:
        if char == ' ':
            continue
        if char in text_dict:
            text_dict[char] += 1
        else:
            text_dict[char] = 1
        char_count += 1
    print(f"{text_dict}\ntotal count: {char_count}")
    return text_dict, char_count


def main():
    text = input("Enter text: ")
    textFrequency(text)


if __name__ == "__main__":
    main()
