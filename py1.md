##BASICS-1
1. for one line comments `#comment`   
   for multi-line comments `""" comment"""`       
2. to print on screen `print" "`     
3. aritmetic operations `+,-,*,/,%,**`   
4. to create variable, just type name of var `x=3 y=2.7`      
5. to create  string type name of string  `a="strr"`   
6. to print string more than once  `print a*8`   
7. to combine two strings, add + between them `print a+b`
8. to get any char from a string at index `strName[index]`
9. to import a module type `import module_name` to top    
10. Pause amount of time, import time and type `time.sleep(5)`   
11. to get legth of string  `len(a)`
12. to print numbers in any range    
```python   
print range(15)
print range (start,end,increase quantity 1 by default)
```   
   
13. **In**    
	```python
	a = "tardis"
	c = 'e' in a #if there is a in tardis returns true 
	```    
14. Type function returns type of its input
`type("asdfg")` returns str   
`type(54)` returns int


**CODE**
```python
#!usr/bin/python
#This is Comment!!!
import time
print"Helloooo!"


#_______________ARITHMETIC OPs___________________________

print 2+2   #prints 4 
print "2+2" #prints 2+2
print "2+2 = ",2+2 #Do not forget to put COMMA

print "10/3 = ", 10/3   #prints 3 
print "10/3 = ", 10/3.0 #prints 3.33333333333
print 2**3  	#prints 8
print 16**0.5   #prints 4

x = 5.2
y = 3.7
z = x+y
print x+y   #prints 8.9
print z		#prints 8.9


#____________STRINGS__________________________________



a = "Helloooo "
b = "woooorld!"
print a            #prints hellooooo
print a*7          #prints hellooooo 7 times
print a+b  	       #prints combination of a and b
print (a+b+"\n")*5 #prints combination of a and b and new line, 7 times


c = "asdfghjkl"
print c[4] + c[0] #prints ga (starts from 0)
print c[1:5]      #prints from index 1 to 5 (sdfg)
print c[:3]  	  #prints asd (starts from 0 by default)
print c[2:]		  #prints dfghjkl (ends with end of string by default)

print len(c) 		#prints 9
print len("github") #prints 6

d = str(21) #d is string now
print "It is " + d 

e = 65
print"asa" + `e`   #converts e to string


#_______________TIME MODULE_________________
time.sleep(2)     #Pause 2 sec
print "asdfghjkl"

#Pause 1 sec in each turn
x=0
while x<=10: 
	print x
	x=x+1
	time.sleep(1)

#_____________RANGE_______________
print range(15) 	 #prints numbers from 0 to 15
print range (7,53)   #prints numbers from 7 to 53
print range (7,53,3)




```
