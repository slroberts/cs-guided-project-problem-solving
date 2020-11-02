"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    """
    a function that return the number (count) of vowels in a given string.
    """
    input_str.lower()
    vowels = "a,e,i,o,u"
    # Check if string contains a vowel "a, e, i, o, or u"
    vowel_count = [v for v in input_str if v in vowels]
    # return the count of the vowels
    return len(vowel_count)


print(get_count("The input string will only consist of lower case letters and spaces"))