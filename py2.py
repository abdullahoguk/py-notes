#!usr/bin/python
import os
import datetime
import time
#___________________WHILE LOOP___________________
x=0
while x<=100 :
	print x
	x=x+5 


print "end of loop"

time.sleep(1)
#Print animated text
z="Welcome to My Universe!!!"
t=0
while t <= len(z):
	os.system("clear")
	print z[:t]
	time.sleep(.15)
	t=t+1


#___________________FOR LOOP______________________

for y in range(1,17,3):
	print "y is ", y




#___________________CALLING SYS COMMAND____________
print "print via python"
os.system("echo 'print via Bash'") #prints in cli via bash
#os.system("sudo apt-get update") #update repos


#_________________DATETIME____________
today = datetime.date.today()
print "today is", today

temp=datetime.timedelta(days=1) #returns 1 day
print "tomorrow is", today+temp #prints tomorrow

print today.strftime("Today is %m/%d/%Y %A %B")



fitr=datetime.date(2015,7,17)
print "Eid al Fitr is ",fitr
left=fitr-today
print left,"left to Eid al Fitr"





