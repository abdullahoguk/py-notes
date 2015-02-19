##BASICS
* Lists 
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