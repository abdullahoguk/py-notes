#!usr/bin/python


#___________________GETTING INPUT___________________
in1 = input("Write Number: ") #Can be used to get numbers. But not strings.Use it for expression like comparing, summation...
in2 = raw_input("Write something: ")#can be used for writing strings. 
print "You wrote 1st : ",in1
print "You wrote 2nd : ",in2

x = int(raw_input("Enter a number: ")) #Can be used to get numbers
print x+58

#___________________TYPE CASTING___________________

#-------- Str>>Int --------
a = "13"
b = 5
print int(a) + b #a is an int now, prints 18
print a + `b` #prints 135

#-------- Int>>Str --------
c = str(21) #d is string now
print "It is " + c 

d = 65
print"It is " + `d`   #converts e to string

e="14"
print "It is " + e

#-------- Int>>Float --------
f=15
print float(f)


#___________________CONDITIONAL STATEMENTS___________________
in3 = input("Write the bigger number less than 100: ")
if in3 == 99:
	print "Well Done!!!"
elif in3>99:
	print "too high"
elif in3<99:
	print "too low"
	#print "You get it Wrong!!!"






