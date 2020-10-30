"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.

# loop through numbers list to get the index - i of each number - n with `enumerate()` -- method adds a counter to an iterable and returns it in a form of enumerate object.
# append (i + n) to a new-list -- new_list.append(i + n)
# return new_list

"""


def add_indexes(numbers:int) -> int:
    """
    a function that returns the list with each element's index in the list added to itself.
    """

    new_list = []
    # loop through numbers list to get the index - i of each number - n with `enumerate()`
    for i, n in enumerate(numbers):
        # append (i + n) to a new-list -- new_list.append(i + n)
        new_list.append(i + n)
    # return new_list
    return new_list 

print(add_indexes([0, 0, 0, 0, 0])) # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5])) # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1])) # ➞ [5, 5, 5, 5, 5]
