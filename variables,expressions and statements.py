Python 3.8.4rc1 (tags/v3.8.4rc1:6c38841, Jun 30 2020, 15:17:30) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #constants
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('hello world')
hello world
>>> #variables
>>> a=35.0
>>> b=12.50
>>> c=a*b
>>> print(c)
437.5
>>> #sentences or line
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> #assignment statesment
>>> x=0.6
>>> x=3.9*x*(1-x)
>>> print(x)
0.9359999999999999
>>> #expressions
>>> #numeric
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> #precedence rules
>>> x=1+2**3/4*5
>>> print(x)
11.0
>>> #operator
>>> eee='hello'+'there'
>>> print(eee)
hellothere
>>> #type matter
>>> eee='hello'+'there'
>>> eee=eee+1
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    eee=eee+1
TypeError: can only concatenate str (not "int") to str
>>> type(eee)
<class 'str'>
>>> type('hello')
<class 'str'>
>>> type(1)
<class 'int'>
>>> #type convertion
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<class 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> #integer division
>>> print(10/2)
5.0
>>> print(99.0/100.0)
0.99
>>> #user input
>>> nam=input('who are you?')
who are you?
>>> print('welcome',nam)
welcome 
>>> 