# A function to select the max value between a and b
def max(a,b):
	"""
	fruitful function select the max value between a and b
	parameter:
			a:the first number
			b: the second number
	returns: the larger number between a and b
	precondition: 
			a and b are integars or float
	"""

	# check if a is less than b
    if(a<b):
        mval =b
    # check if a is greater equal than b
    else:
        mval=a
    return mval
    
#test cases and function call
a=1.0
b=2.0
c=max(a,b)
d=max(b,a)