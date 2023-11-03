"""  
A function to search for the first vowel position

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns -1 if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns -1
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """

    result=len(s)
    temp=introcs.find_str(s,"a")
    if temp != -1 and temp<result:
        result = temp
    temp=introcs.find_str(s,"e")
    if temp != -1 and temp<result:
        result = temp
    temp=introcs.find_str(s,"i")
    if temp != -1 and temp<result:
        result = temp
    temp=introcs.find_str(s,"o")
    if temp != -1 and temp<result:
        result = temp
    temp=introcs.find_str(s,"u")
    if temp != -1 and temp<result:
        result = temp
    temp=introcs.find_str(s[1:],"y")
    if temp != -1 and temp<result:
        result = temp+1
    return -1 if result =len(s) else result


test=first_vowel("hat")
print(test)
test2=first_vowel("grrm")
print(test2)
