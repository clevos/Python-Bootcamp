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

    # save string (s)length in a variable called result
    result=len(s)
    # find location of character a in string s
    temp=introcs.find_str(s,"a")
    # if the character is  found and character location less than length of the string
    if temp != -1 and temp<result:
        #update the result with the character location saved in temp
        result = temp
    temp=introcs.find_str(s,"e")
    # if the character is  found and character location less than length of the string
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
    # if variable result keeps original value means there no vowel character found in string
    # else return the location or index of that character
    return -1 if result =len(s) else result

# test case and function call
test=first_vowel("hat")
print(test)
test2=first_vowel("grrm")
print(test2)
