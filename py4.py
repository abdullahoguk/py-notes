#!usr/bin/python
from collections import OrderedDict


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


del dict1[16]
print "16 : Bursa removed "
print dict1

print dict1.get(16,"This element is not exist")
print dict1.get("06","This element is not exist")

dict1.clear()
print "All elements removed"
print dict1


#__________________ORDEREDDICTS____________________

oDict = OrderedDict([("01", "Adana"),("02", "Adiyaman"), ("03", "Afyon")])
print oDict

oDict["04"] = "Agri"
oDict["05"] = "Amasya"
print oDict

print "Keys are ", oDict.keys()
print "Values are ", oDict.values()

print oDict.get(16,"This element is not exist")
print oDict.get("05","This element is not exist")