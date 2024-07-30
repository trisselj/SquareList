# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/30/2024
# Description: takes as a parameter a list of numbers and replaces each value with the square of that value

# Defines an input method to square a list
def square_list(numbers):
    for i in range(len(numbers)): # Modifies the list by squaring without returning a value
        numbers[i] = numbers[i] ** 2