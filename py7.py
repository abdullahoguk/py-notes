#!usr/bin/python
import re
#___________________REGULAR EXPRESSIONS___________________
print "-----------REGULAR EXPRESSIONS------------------"
#match method
a = "Python is the best"
print re.match("Python", a) #returns "<_sre.SRE_Match object at 0x7f017522a308>"
print re.match("C", a) #returns "None"
print re.match("best", a) #returns "None"

print re.match("Python", a).group() #returns "Python"


#search method
print re.search("Python", a) #returns "<_sre.SRE_Match object at 0x7f017522a308>"
print re.search("C", a) #returns "None"
print re.search("best", a) #returns "<_sre.SRE_Match object at 0x7f017522a308>"

print re.search("Python", a).group() #returns "Python"
print re.search("best", a).group() #returns "best"


#findall method
print re.findall("e", a) #returns all e's in string
