#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [num for num in num_list if num % 2 == 0]
    return even_list


def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]


print(return_evens([2, 5, 6, 8, 9, 10]))
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))