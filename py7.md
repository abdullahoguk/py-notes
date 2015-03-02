##BASICS-7
* **Regular Expressions**
	* First `import re`
	* `match("Python", str)` if str starts with "Python",returns object(can be printed by using `re.match("Python", str).group()`)
	* `search("Python", str)` if str contains "Python",returns object(can be printed by using `re.search("Python", str).group()`) 
	* `findall("e", str)` to find all "e"s in str
   
	* Metacharacters([], ., \, *, +, ?, {}, ^, $, |, ())
		* **[]** control a letter one by one
			`re.search("[fm]ail",str)` if str contains "fail" or "mail", returns object.   
			`re.match("[A-Z][0-9][A-Z]",str)` if str starts with a capital letter followed by a number then a capital letter again, returns object.   
		* **.** represent all charaters except new line. just one char   
			`re.match(".ail",str)` if str starts with any char followed by "ail", returns object.
		* `*` (Kleene star) the preceding char can repeat 0 or more times 
			`re.match("hello*",str)` if str starts with "hell" or "hello" or "helooo"..., returns object.   
			`re.match(".*body", str)` any str ends with "body" will be returned.  
		* **+** pretty same with Kleene star, but the preceding should repeat at least one time.
		* **?** pretty same with * and +, but the preceding should repeat just 0 or 1 times.
		* **{}** the preceding char's repetition times defined insid curly brackets
			`re.match("hello{5}",str)` 'o' repeat 5 times. Returns object when str starts with 'hellooooo'   
			`re.match("hello{1,4}",str)` 'o' repeat at least 1, at most 4 times.   
		* **^** starts with...
		when used with search(), it becomes match() `match("Python", str)` = `search("^Python", str)`      
		It also means 'except' when used with '[]'    
		`re.match("[0-9a-z][^A-Z]+",str)` returns object when str starts with any number or lower case letter that does not followed by any (1 or more) capital letters.
		* **$** ends with...
		* `\` escape character
		* **|** or    
		`re.search("^fa|ce$",str)` returns object if str starts with fa or ends with ce
		* 


