Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #conditional execution
>>> x=5
>>> if x<10
SyntaxError: invalid syntax
>>> if x<10 print('smaller')
SyntaxError: invalid syntax
>>> if x<10:
	print('smaller')

	
smaller
>>> if x>20:
	print('bigger')

	
>>> print('finish')
finish
>>> #comparision operators
>>> x=5
>>> if x==5 :
	print('equals 5')

equals 5
>>> if x>4:
	print('greater than 4')

	
greater than 4
>>> #nested decisions
>>> x=42
>>> if x>1:
	print('more than one')
	if x<100:
		print('less than 100')
print('all done')
SyntaxError: invalid syntax
>>> print('all done')
all done
>>> if x>1:
	print('more than one')
	if x<100:
		print('less than 100')

		
more than one
less than 100
>>> #two-way
>>> x=4
>>> if x>2:
	print('bigger')
	else:
		
SyntaxError: invalid syntax
>>> x=4
>>> if x>2:
	print('bigger')
	
SyntaxError: multiple statements found while compiling a single statement
>>> x=4
>>> if x>2:
	print('bigger')
	
SyntaxError: multiple statements found while compiling a single statement
>>> #multi-way
>>> if x<2:
	print('small')

	
>>> elif x<10:
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> if x<2:
	print('small')
	elif x<10:
		
SyntaxError: invalid syntax
>>> #try /except
>>> astr='bob'
>>> try:

	print('hello')
	istr =int(astr)
	print('there')
>>>except:
	
SyntaxError: invalid syntax
>>> 