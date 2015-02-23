##BASICS-4
* **Lists** 
	* to create list `list_name [e1,e2,...]`    
	* `len()` can be used for getting how many elements in the list    
	* to append an elemnet(just one) to list `list_name.append(element)`
	* each element has index that starts from 0   
	  to get an elment from any index `list_name[index]`   
	  to get Last element `list_name[-1]`   
	* to insert an elemnet(just one) to list `list_name.insert(insert_index , element)`  
	* to extend or combine two list `list_name.extend(append_list_name)`     
		this command is same with `list_name = list_name + append_list_name)`   
	* to remove an element from the list `list_name.remove(element)` or `del list_name[2]`
	* to pop an element `list_name.pop()` this method return last element and removes it.   
	  Also can be used as `list_name.pop(index)` to pop from any index.
	* to find index of any element `list_name.index(element)`   
	* to sort list alphabeticly `list_name.sort()`   
	* to reverse elements' index `list_name.reverse()`
	* to get how many times an element in the list `list_name.count(elemet)`   
   
* **Tuples**
	* tuple is like list, but you can't perform an operation like sorting,removing, adding,inserting...
	* to create a tuple     
	`tup = "pyt", "java", 1, 25`      
	or        
	`tup = ("pyt", "java", 1, 25)`      
	* to create empty tuple `tup = ()`   
	* to create tuple tat has 1 element `tup = ("element",)`   
	* to get element in tuple  `tuple_name[index]`   
	* to unpack tuple `variables as much as tuples length = tuple_name`      
	eg : if there is 3 element in the tuple `el1, el2, el3 = tuple_name`   
   
* **Dicts**
	* Dicts includes key and values
	* to create a dict `dict_name{"key1" : "value1", "key2" : "value2" ...}`
	* to get an element with any key `dict_name["key"]`    
	* Small numbers can be written without quotation mark (shouldn't start with 0)        
 	* to delete an element `del dict_name["key"]`   
 	* to remove all elements `dict_name.clear()`
 	* to get all keys `dict_name.keys()`
 	* to get all values `dict_name.values()`
 	* to get all elements `dict_name.items()`    
    
* **OrderedDict**
	* Normal dicts are not sorted by adding order
	* to use OrderedDict we should import from collections `from collections import OrderedDict`   
	* to create a dict `dict_name = OrderedDict([("key1", "value1"),("key2", "value2"), ("key3", "value3", ...)])`
	* to add element `dict_name["key"] = "value"`   

**CODE**
```
#!usr/bin/python
from collections import OrderedDict


#___________________LISTS___________________
print "#___________________LISTS___________________"

bCities=["Istanbul",34,"Ankara",06,"Izmir",35]

print bCities
print "There are ",len(bCities)," elements in the list"

bCities.append("Bursa")
bCities.append(16)

print "Bursa added", bCities
print bCities[0],bCities[2],bCities[4],bCities[6]
print "Last element is ", bCities[-1]

bCities.insert(2,"Ordu")
bCities.insert(3,52)
print "Ordu inserted",bCities

bCities2 = ["Manisa",45,"Rize",53]

print "Cities 2 is ", bCities2
bCities.extend(bCities2)
print "Cities extended with Cities 2 ",bCities

last1 = bCities.pop()
last2 = bCities.pop()
print "The last 2 element is ",last2, "and" , last1 ,", and they are removed "
print bCities

print "Ordu is in index ", bCities.index("Ordu") 

bCities.sort()
print "Sorted list is ", bCities

bCities.reverse()
print "Reversed list is ", bCities

bCities.append("Ankara")
print "Ankara is ", bCities.count("Ankara"), " times in the list"
print bCities
#TODO use for to iterate list


#___________________TUPLES____________________
print "___________________TUPLES____________________"
tup1 = 1,5,13,"number"
tup2 = ("a","b","c")
tup3 = ("x",) 
tup4 = ("y") #not tuple
print "tup1 is a ",type(tup1)
print "tup2 is a ",type(tup2)
print "tup3 is a ",type(tup3)
print "tup4 is a ",type(tup4)

print tup1[1], "is in tup1's index 1"

a, b, c, d = tup1 #unpack tuple 
print a, b, c, d
print tup1


#___________________DICTS____________________
print "___________________DICTS____________________"

dict1 = {"06":"Ankara", 34:"Istanbul", 35:"Izmir", 52:"Ordu", 16:"Bursa"} #Nubers is the Licence plates of cities
print "dict 1 is a ", type(dict1)
print dict1
print "06 is licence plate of ",dict1["06"]
print "34 is licence plate of ",dict1[34]
print "35 is licence plate of ",dict1[35]
print "52 is licence plate of ",dict1[52]
print "16 is licence plate of ",dict1[16]


print "Keys are ", dict1.keys()
print "Values are ", dict1.values()
print "All items are ",dict1.items()

del dict1[16]
print "16 : Bursa removed "
print dict1

print dict1.get(16,"This element do not exist")
print dict1.get("06","This element do not exist")

dict1.clear()
print "All elements removed"
print dict1


#__________________ORDEREDDICTS____________________
print "__________________ORDEREDDICTS____________________"
oDict = OrderedDict([("01", "Adana"),("02", "Adiyaman"), ("03", "Afyon")])
print oDict

oDict["04"] = "Agri"
oDict["05"] = "Amasya"
print oDict

print "Keys are ", oDict.keys()
print "Values are ", oDict.values()

print oDict.get(16,"This element do not exist")
print oDict.get("05","This element do not exist")
```