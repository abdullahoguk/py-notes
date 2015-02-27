##BASICS-6

* **String Methods**
	* `capitalize()` capitilize first letter of string.(github >> Github)
	* `upper()` makes all letters uppercase  (github >> GITHUB)
	* `lower()` makes all letters lowercase  (GITHUB >> github)
	* `swapcase()` swaps all letter's cases (GitHuB >> gIThUb)
	* `title()` makes initial letter of all words uppercase (py programming >> Py Programming)
	* `center()` centered ("py".center(4, "#") >> #py#) ("py".center(6)>> '  py  ')
	* `ljust()` align left ("py".ljust(5,"#")>> 'py###')
	* `rjust()` align right ("py".rjust(5,"#")>> '###py')
	* `replace(char to change,new char)`  
		* `"programming".replace("r","a")` >> `paogaamming`
		* Can be used to delete chars `"programming".replace("r","")` >> `pogamming`
		* You can select how many chars should be changed. `"suppress".replace("s","#",2)` >> `#upre#s`
		* Upper and lower cases of same letter are different character.
	* `startswith(chr)` returns true if string starts with 'chr'.
	* `endswith(chr)` returns true if string ends with 'chr'.
	* `count(chr)` returns how many 'chr' character in the string.

	* `isalpha()` return true if string has only alphabetic chars.(does not contain any numerical character or symbol). 
	* `isdigit()` return true if string has only numerical chars.(doesn't contain any alphabetical character or symbol). 
	* `isalnum()` return true if string has both alphabetical and numerical chars. (does not contain any symbol). 
	* `islower()` returns true if all chars in string is lower case.
	* `isupper()` returns true if all chars in string is upper case.
	* `istitle()` returns true if string is in title form. 
	* `isspace()` returns true if all chars in string is space.
	   
	* `expandtabs(10)` expand tabs (\t) in string to given size. 

	* `find(chr)` returns first index of 'chr'.If string does not contain it, returns '-1'
	* `find(chr,beginning,end)` returns first index of 'chr' in given interval.
	* `rfind(chr)` reverse of find(). Starts searching from right. If string does not contain it, returns '-1'
	* `index(chr)` like find().returns first index of 'chr'
	* `index(chr,beginning,end)` returns first index of 'chr' in given interval.
	* `rindex(chr)` like rfind(). Starts searching from end of string.
    
	* `"x".join(str)` inserts x between each two chars of str.`"*".join(python)`>> `p*y*t*h*o*n`
	* `partition(chr)` divide string  a.partition("an")` >> `('ist', 'an', 'bul')`
	* `partition(chr)` reverse of partition()
	* `strip()` delete spaces and new lines from beginning and end of the string
	* `rstrip()` delete spaces and new lines from just end of the string
	* `lstrip()` delete spaces and new lines from just beginning of the string
	* `str = u"ğüşç"` creating a unicode str. If your string contains, unicode character, string methods does not work correctly it str did not created as unicode.
	