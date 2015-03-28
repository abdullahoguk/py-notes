#!usr/bin/python

import os
#___________________FUNCTIONS_______________________
print "-------------FUNCTIONS-------------\n"
def factorial(a):
	if a == 0:
		return 1
	else:
		return a*factorial(a-1)

print "9! is ",factorial(9)		



def pr():
	a=3
	global b 
	b = 7
	print "a and b is :",a,b

pr()
#print "a is ",a > gives err, a is declared in func body
print "b is ",b

#TODO use for to iterate list

#______________________MODULES_________________________
print "\n--------------MODULES----------------\n"
print "You can use foolowing functions from os module", dir(os) #return available functions, fields ... in os module

if os.name =="posix":
	print "You are using a Linux distro"
if os.name =="nt":
	print "You are using Windows"


#return all files located in "/home/abdullah/Documents"
print "All files located in ""/home/abdullah/Documents"""
x = os.listdir("/home/abdullah/Documents")
for files in x:
	print files



print os.getcwd() #return directory of file
print "Files in current directory are ", os.listdir(os.curdir)

#os.chdir("/var/tmp") > changes curr dir
#os.mkdir("new") > creates new folder in curr dir
#os.makedirs("/home/abdullah/newfolder1/newfolder2") > removes two folders in a time
#os.mkdir("dir") > removes "dir" folder in curr dir
#os.makedirs("/home/abdullah/newfolder1/newfolder2") > removes two folders in a time

print "Seperators using for directories in this OS is ", os.sep
#os.makedirs("dir1" + os.sep + "dir2") #this line runs in multiple OSes
#os.makedirs(os.sep.join([dir2, dir3])) 

#____________________FILES________________________
print "\n----------------FILES-----------------\n"
file1 = open("test.txt", "a")
file1.write("Hello")
#file1.close() >> after close file, you cannot write to file
file1.write("\nWorld!\n\n")


list1 = ["Python", "C++", "Java", "Ruby"]
for i in list1:
	file1.write(i+"\n")
file1.close()



readfile = open("test.txt", "r")
print "Content of file is in following\n", readfile.read() #read all file
readfile.seek(0)

print readfile.readlines()
readfile.seek(0)

print readfile.readline() #read line start from where cursor is
readfile.seek(14)
print "Start from 14th char to /n >>", readfile.readline() #read line start from 14th character

print "All lines after 5th line >> ", readfile.readlines(5) #read all lines start from 5th line

print "Cursor is in ", readfile.tell() 

#os.remove("test.txt") #removes file


#___________________EXCEPTION HANDLING___________________
print "\n------------EXCEPTION HANDLING-------------\n"

try:
	dividend = int(raw_input("Enter dividend for division: "))
	diveder = int(raw_input("Enter diveder for division: "))
	result = float(dividend) / diveder
	print dividend,"/", diveder,"=", result
except ZeroDivisionError:
	print "Do not try to divide by 0!"
except ValueError:
	print "Enter a valid input!"

