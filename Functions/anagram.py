#!/usr/bin/env python3
"""Check that words are anagrams. An anagram of an word
is one formed by rearranging the letters of the words"""


def anagramChecker(word1, word2):
    """Anagram checker"""
    if len(word1) != len(word2):
        print(f"{word1} and {word2} are not equal in length\
 and are not anagrams")
        return False
    word_dict = {}

    for char in word1:
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1

    for char in word2:
        if char in word_dict:
            word_dict[char] -= 1
            if word_dict[char] < 0:
                print(f"{word1} and {word2} are not anagrams")
                return False

    print(f"{word2} is an anagram of {word1}")
    return True


def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    anagramChecker(word1, word2)


if __name__ == "__main__":
    main()
