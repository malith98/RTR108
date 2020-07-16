Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##
>>> #strings
>>> 
>>> strl='hello'
>>> str2='there'
>>> bob=strl + str2
>>> print()bob
SyntaxError: invalid syntax
>>> print(bob)
hellothere
>>> str3='123'
>>> str3=str3 +1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    str3=str3 +1
TypeError: can only concatenate str (not "int") to str
>>> x=int(str3)+1
>>> print(x)
124
>>> name=input('enter:')
enter:chuck
>>> print(name)
chuck
>>> x=int(apple)-10
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=int(apple)-10
NameError: name 'apple' is not defined
>>> #
>>> ##
>>> fruit='banana'
>>> letter=fruit[1]
>>> print(letter)
a
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>> x=len(fruit)
>>> print(x)
6
>>> word='banana'
>>> count=0
>>> for letter in word :
	if letter=='a':
		count=count+1
print(count)
SyntaxError: invalid syntax
>>> for letter in word :
	if letter=='a':
		count=count+1print(count)
		
SyntaxError: invalid syntax
>>> #
>>> ##
>>> ###slicing strings
>>> ##
>>> #
>>> s='monty python'
>>> print(s[0:4])
mont
>>> print(s[6:7])
p
>>> print(s[6:20])
python
>>> print(s[:])
monty python
>>> 
>>> 
>>> 
>>> 
>>> a='hello'
>>> b=a+'there'
>>> print(b)
hellothere
>>> c=a+''+'there'
>>> print(c)
hellothere
>>> #
>>> ##
>>> ###
>>> ##
>>> #
>>> fruit='banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> if 'a' in fruit:
	print('found it')

	
found it
>>> 
>>> 
>>> 
>>> greet='hello bob'
>>> zap =greet lower()
SyntaxError: invalid syntax
>>> zap = greet.lower()
>>> print(zap)
hello bob
>>> print('HI THERE'.lower())
hi there
>>> 
>>> 
>>> 
>>> stuff='hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> fruit='banana'
>>> pos=fruit.find('na')
>>> print(pos)
2
>>> aa=fruit.find('z')
>>> print(aa)
-1
>>> 
>>> 
>>> 
>>> 
>>> line='please have a nice day'
>>> line.startswith('please')
True
>>> line.startswith('p')
True
>>> 