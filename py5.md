##BASICS-4
* **Functions**
	* to define a function 
	```
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
		* `from modül_adı import *`	
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
**CODE**
```
```