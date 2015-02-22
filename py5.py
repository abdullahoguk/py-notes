#!usr/bin/python
import os
#___________________FUNCTIONS___________________

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

#TODO use for to iterate

#___________________MODULES___________________
print dir(os) #return os name

if os.name =="posix":
	print "You are using a Linux distro"
if os.name =="nt":
	print "You are using Windows"


#return all files located in "/home/abdullah/Documents"
x = os.listdir("/home/abdullah/Documents")
for files in x:
	print files



print os.getcwd() #return directory of file
print "File in current directory are ", os.listdir(os.curdir)

#os.chdir("/var/tmp") > changes curr dir
#os.mkdir("new") > creates new folder in curr dir
#os.makedirs("/home/abdullah/newfolder1/newfolder2") > removes two folders in a time
#os.mkdir("dir") > removes "dir" folder in curr dir
#os.makedirs("/home/abdullah/newfolder1/newfolder2") > removes two folders in a time

print "Seperators using for directories in this OS is ", os.sep
#os.makedirs("dir1" + os.sep + "dir2") #this line runs in multiple OSes
#os.makedirs(os.sep.join([dir2, dir3])) 