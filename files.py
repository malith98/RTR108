Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ####files
>>> ###
>>> ##
>>> #
>>> fhand=open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    fhand=open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> 
>>> 
>>> stuff='hello\nworld'
>>> stuff
'hello\nworld'
>>> print(stuff)
hello
world
>>> stuff='X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> 
>>> 
>>> xfile=open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    xfile=open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> 