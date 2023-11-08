"""  
A function to extract names from e-mail addresses.

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.
    
    We assume (see the precondition below) that the e-mail address is in one of
    two forms:
        
        last.first@megacorp.com
        first.last@mompop.net
    
    where first and last correspond to the person's first and last name.  Names
    are not empty, and contain only letters. Everything after the @ is guaranteed 
    to be exactly as shown.
    
    The function preserves the capitalization of the e-mail address.
    
    Examples: 
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'
    
    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    # You must use an if-else statement in this function.
    #pass

    # find location of "@" in the string s using the introcs package
    pos=introcs.find_str(s,"@")
    
    # get the domain after the @ symbol
    domain=s[pos:]

    # the string before the @ symbol is the username
    user=s[0:pos]
    
    #check the domain name = mompop.net
    if domain =="@mompop.net":
        print("fullname:",user)
        #in this domain the user first name and last is separated by the dot
        pos1=introcs.find_str(user,".")
        print("firstname",user[0:pos1])
        result=user[0:pos1]
    #raise a error if the domain is not matched
    else:
        print("error")
        print("fullname ",user)    
        pos2=introcs.find_str(user,".")
        print("firstname",user[pos2+1:])
        result=user[pos2+1:]
        #return result
    return result

#test case and function call
test=extract_name("first.last@mompop.net")
print(test)
print("==============")
test2=extract_name('smith.john@megacorp.com')
        
