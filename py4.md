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
	* to remove an element from the list `list_name.remove(elment)` 
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
    
* **OrderedDict**
	* Normal dicts are not sorted by adding order
	* to use OrderedDict we should import from collections `from collections import OrderedDict`   
	* to create a dict `dict_name = OrderedDict([("key1", "value1"),("key2", "value2"), ("key3", "value3", ...)])`
	* to add element `dict_name["key"] = "value"`   

**CODE**
```
#!usr/bin/python

#___________________LISTS___________________
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

#___________________TUPLES____________________

```