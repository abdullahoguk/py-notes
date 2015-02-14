##BASICS
1. for comments `#`      
2. to print on screen `print" "`     
3. aritmetic operations `+,-,*,/,%`   
4. to create variable, just type name of var `x=3 y=2.7`      
5. to create  strng type name of string  `a="strr"`   
6. to print string more than once  `print a*8`   
7. to combine two strings, add + between them `print a+b`
8. to get any char from a string at index `x c[x]`
9. to import a module type `import module_name` to top    
10.Pause amount of time, import time and type `time.sleep(5)`   






**CODE**
```
#!usr/bin/python
#This is Comment!!!
import time
print"Helloooo!"


#__________ARITHMETIC OPs_________________________________

print 2+2   #prints 4 
print "2+2" #prints 2+2
print "2+2 = ",2+2 #Do not forget to put COMMA

print "10/3 = ", 10/3   #prints 3 
print "10/3 = ", 10/3.0 #prints 3.33333333333

x = 5.2
y = 3.7
z = x+y
print x+y   #prints 8.9
print z		#prints 8.9


#__________STRINGS__________________________________



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



#_______________TIME MODULE_________________
time.sleep(2)     #Pause 2 sec
print "asdfghjkl"

#Pause 1 sec in each turn
x=0
while x<=10: 
	print x
	x=x+1
	time.sleep(1)







```
