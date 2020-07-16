Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #functions
>>> def things():
	print('hello')
	print('fun')

	
>>> thing()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    thing()
NameError: name 'thing' is not defined
>>> def things():
	print('hello')
	print('fun')
things()
SyntaxError: invalid syntax
>>> def things():
	print('hello')
	print('fun')
	thing()
	print('zip')
	thing()

	
>>> big=max('hello world')
>>> print(big)
w
>>> tiny=min('hello world')
>>> print(yiny)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(yiny)
NameError: name 'yiny' is not defined
>>> print(tiny)
 
>>> #type conversions
>>> print float(99)/100
SyntaxError: invalid syntax
>>>  print float(99) / 100
 
SyntaxError: unexpected indent
>>> i =42
>>> type(i)
<class 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<class 'float'>
>>> print(1+2*float(3)/4-5)
-2.5
>>> #string conversions
>>> sval='123'
>>> type(sval)
<class 'str'>
>>> print(sval+1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(sval+1)
TypeError: can only concatenate str (not "int") to str
>>> #
>>> ##
>>> ###build own code
>>> ##
>>> #
>>> x=5
>>> print('hello')
hello
>>> x=5
>>> print('hello');
hello
>>> def print_lyrics():
	print('i am a lumberjack,i am okay')
	print('i sleep all night and i work all day')
print('yo')
SyntaxError: invalid syntax
>>> #
>>> #parameter
>>> #
>>> def greet(lang):
	if lang=='es':
		print('hola')
	elif lang=='fr':
		print('bonjour')
	else:
		print('hello')

		
>>> greet('en')
hello
>>> greet('es')
hola
>>> greet('fr')
bonjour
>>> 