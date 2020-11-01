"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
def max_and_min(input_str):
    """
    a function that returns the maximum and minimum integers.
    """

    # convert input_str to list 
    int_list = list(input_str.split(' ') )
    
    # find max and min with max() and min()
    max_integer =  max(int_list)
    min_integer =  min(int_list)

    # concatenate max_integer and min_integer
    return  max_integer + " " + min_integer
     

print(max_and_min("1 2 3 4 5")) # -> "5 1"
print(max_and_min("1 2 -3 4 5")) #  -> "5 -3"
print(max_and_min("1 9 3 4 -5")) # -> "9 -5"
