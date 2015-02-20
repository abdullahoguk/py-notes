#!usr/bin/python
#This is Comment!!!
"""
This 
is
also
comment 
"""

import time
print"Helloooo!"


#____________ARITHMETIC OPs_________________________________

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
print"asa"+ `e`   #converts e to string
 


#_________________TIME MODULE_________________
time.sleep(2)     #Pause 2 sec
print "asdfghjkl"

#Pause 1 sec in each turn
x=0
while x<=10: 
	print x
	x=x+1
	time.sleep(1)


#_______________RANGE_______________
print range(15) 	 #prints numbers from 0 to 15
print range (7,53)   #prints numbers from 7 to 53
print range (7,53,3)

