Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while true:
	ilne=input('>')
	if line=='done':
		break
	print(line)

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    while true:
NameError: name 'true' is not defined
>>> print('done')
done
>>> while true:
	line = raw_input('>')
	if line(0)=='#':
		continue
	if line=='done':
		break
	print(line)
    print('done')
    
SyntaxError: unindent does not match any outer indentation level
>>> while true
SyntaxError: invalid syntax
>>> for i in[5,4,3,2,1]:
	print(i)
	print('blastoff')

	
5
blastoff
4
blastoff
3
blastoff
2
blastoff
1
blastoff
>>> 
>>> 
KeyboardInterrupt
>>> for i in[5,4,3,2,1]:
	print(i)

	
5
4
3
2
1
>>>  for i in[5,4,3,2,1]
 
SyntaxError: unexpected indent
>>> ##loop idiom
>>> 
>>> 
>>> print('before')
before
>>> print('before');
before
>>> print('before')
for thing in [9,41,12,3,74,15]:
	
SyntaxError: multiple statements found while compiling a single statement
>>> 