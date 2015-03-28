##BASICS-5
* **Functions**
	* to define a function 
	```python
	def function_name():
		function
		body
		as intended
	```
	* We have a function like `def function_name(name,surname,number):`
		* we should normally enter parameters respectively. `function_name("John","Watson",15):`
		* if we know the names of parameters, function can be called as    
			`function_name(surname="Watson", number=15, name = "John"):`   
	* Variabales that declared in function body can't be used out of function   
		to use a variable out of function, variable should declared as global `global var_name`
    

* **Modules**
	* In python, the file that has '.py' extension is also a module
	 
	* to import module
		* `import module_name`
			to call a function `module_name.func_name()` 
		* `from module_name import *`	
			to call a function `func_name()`
		* `from module_name import func_name1, func_name2, var1, ...`    
			to call a function `func_name()`
		* import module_name as new_name
			to call a function `new_name.func_name()`
		* to get available functions, fields etc. `dir(module_name)`   

	* os module
		* `os.name` return OS name (for linux "posix": for windows "nt","dos", "ce": for mac "mac") 
		* `os.listdir("/directory/name")` return all files in that directory
			`os.listdir(os.curdir)` lists all files in current directory
		* `os.getcwd()` return current directory (where this file located)
		* `os.chdir("/dir/name")` changes current directory
			os.chdir(os.pardir) changes current directory to parent directory
		* `os.mkdir("/home/directory/name/new_folder") creates new folder in that directory
			os.mkdir("new_file") creates new folder in current directory
		* `os.makedirs("/home/abdullah/newfolder1/newfolder2")` allows to create multiple folders
 		* `os.rmdir("/dir/name")` removes that directory. usage is same with mkdir   
 		* `os.removedirs("dir1/dir2")` allows to remove multiple folders. usage is same with makedirs
		* `os.sep` return seperator that have been using for directories in currrent OS 
   
* **Files**
 	* Create and open file 
 		* `open("test.txt", "w")` creates a file with write permission. (If there is a file with same name, it will override it.)   
 		* `open("test.txt", "r")` creates a file with just read permission (It will give err if there is not such file)
 		* `open("test.txt", "a")` creates a file with append permission. (program do not override file each time)
 		* `open("test.txt")`  creates a file with just read permission by default.
 		* `open("/home/dir/test.txt","w")` creates file in spesific location
 	* files can be assign to a variable `new_file = open("test.txt", "w")`
 	    
 	* Write to file
 		* to write sth to file `filename.write("Hello!")`
 		* after writing, to close the file `filename.close()`
 		* alterntive `filename.writelines(["asd\n", "fgh\n", ...])`
 	   
 	* Read file
 		*    
 		```python
 		readfile = open("test.txt", "r")
		print readfile.read()
		```   
		* after reading, cursor will be in end of file
		* `dosya.seek(0)` moves cursor to beginning of file

		* `filename.readlines()` read lines as list
		* `readfile.readlines(5)` read all lines start from 5th line
		* `filename.tell()` return where the cursor is

	* Remove file 
		os.remove("/file/dir")`

	* to insert line to file
		```python
		readfile = open("test.xml")
		inserted_line = '<Fierce name="Item2.5" separator="," src="myfile25.csv" />'
		filecontent = readfile.readlines() #this line copy all content to filecontent list 
		filecontent.insert(3, insertedline + "\n") #this line insert to list 
		readfile.close()
		writefile = open("test.xml", "w")
		writefile.writelines(filecontent) #this line rewrite all content
		writefile.close()
		```
   
* **Exception Handling**
	* to handle exception (try ... except ...)
	```python
	try:
		ops 
		to try
		as intended
	except Error_Name:
		ops
		to run
		when Error_Name
		error occurs
		as intended
	```   
	* Multiple except blocks can be used.
	```python
	try:
		...
		...
	except Error_Name1:
		...
		...
	except Error_Name2:
		...
		...
	```
	* Multiple errors can be used in one except block.   
	```python   
	except (Error_Name1, Error_Name2):
		...
	```   
	* pass can be used to pass when error occurs
	```python
	try:
		...
	except Error_Name:
		pass
	```




**CODE**
```python
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
```