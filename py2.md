##BASICS-2

* **While Loop**    
```
while a_logical_op:
	type ops that 
	have done in
	each turn
	as intended
```

* **Logical Ops**
```
== : equals
!= : not equal
>  : greater
<  : smaller
>= :greater and equal
<= :smaller and equal
```
* **For Loop**
```
for y in range(start,end,amout of increasing):
	type ops that 
	have done in
	each turn
	as intended

```   
* **Break**
Stops loop. Using with if statements.   

* **Continue**
Stops current turn(skip ops below continue) and go to next turn   
* **To call a command from system** 
import os then `os.system("COMMAND")`     

* **Date Time**    
import datetime 
	* to get todays date `datetime.date.today()`
	* to get tomorrow 

	```
	today = datetime.date.today()
 	temp=datetime.timedelta(days=1)
 	today+temp #returns tomorrow
	```
	* to format date `today.strftime("%m/%d/%Y %A %B")`
	to get a spesific date `datetime.date(2015,12,25)`
