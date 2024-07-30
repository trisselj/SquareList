# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/30/2024
# Description: takes as a parameter a list of numbers and replaces each value with the square of that value

def square_list(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2