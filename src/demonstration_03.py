"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!

Main objective - return the product * of all numbers in the string
- convert number in string to int() and remove the ", "
- then multiply the number and return the result


"""


def multiply_nums(nums):
    """
    a function that returns the product of 2 numbers
    """

    # convert number in string to int() and remove the ", " 
    integers = [int(i) for i in nums.split(", ")]
    # assign the result a value of 1 to multiply the integers 1 by 1
    result = 1
    for n in integers:
        result = result * n
    return result

print(multiply_nums("2, 3")) # ➞ 6
print(multiply_nums("1, 2, 3, 4")) # ➞ 24
print(multiply_nums("54, 75, 453, 0")) # ➞ 0
print(multiply_nums("10, -2")) # ➞ -20
