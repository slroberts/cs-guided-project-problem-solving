"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"

# loop through input_str to using enumerate() to create an index for each letter

# to letter_list we append each letter * by it's (index + 1) to increase the letters ina a pattern -- we have to add 1 for the index numbers to start at 1 instead of 0. if don't add 1 we will start at 0 and the first letter * by zero will be []. 

# capitalize the first letter of every pattern

# join the letters with "-" and convert to str
 
"""
from typing import Literal


def repeat_it(input_str: str) -> str:
    """
    a function that returns a string where each character repeats 
    in an increasing pattern,starting at 1.
    """
    # new list to store letters
    letter_list = []
    # loop through input_str to using enumerate() to create an index for each letter
    for i, letter in enumerate(input_str):
        # to letter_list we append each letter * by it's (index + 1) to increase the letters ina a pattern -- we have to add 1 for the index numbers to start at 1 instead of 0. if don't add 1 we will start at 0 and the first letter * by zero will be []. 
        letter_list.append(letter * (i + 1))
    # capitalize the first letter of every pattern
    letter_list = [letter.capitalize() for letter in letter_list]
    # join the letters with "-" and convert to str
    to_string =  "-".join(str(l) for l in letter_list)
    # return to_string
    return to_string


print(repeat_it("abcd")) # -> "A-Bb-Ccc-Dddd"
print(repeat_it("RqaEzty")) # -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(repeat_it("cwAt")) # -> "C-Ww-Aaa-Tttt"
