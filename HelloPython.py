#!/usr/bin/python
#R00131068gg
import datetime
import re
import sys
import os
# Trigger a remote build
statTime = 8
now = datetime.datetime.now()
# Did i go to Jenkins f

print
print ("Current date and time using str method of datetime object:")
print (str(now))

print
print ("Current date and time using instance attributes:")
print ("Current year: %d" % now.year)
print ("Current month: %d" % now.month)
print ("Current day: %d" % now.day)
print ("Current hour: %d" % now.hour)
print ("Current minute: %d" % now.minute)
print ("Current second: %d" % now.second)
print ("Current microsecond: %d" % now.microsecond)

print
print ("Current date and time using strftime:")
print (now.strftime("%Y-%m-%d %H:%M"))

# Create file and write data

filepath = '/Users/gog/Documents/GitHub/AgileAssessment2/ClockingMachine/shifts.txt'

mode = 'a' if os.path.exists(filepath) else 'w'
with open(filepath, mode) as f:
	if now.hour == statTime:
		f.write(now.strftime("%Y-%m-%d %H:%M(start work)\n"))
	elif (now.hour == statTime and now.minute >= 1):
		print ("You are late today")
		f.write(now.strftime("%Y-%m-%d %H:%M (late)\n"))
	elif now.hour >= (statTime + 6) and now.hour < (statTime + 7):
		print ("See you after lunch")
		f.write(now.strftime("%Y-%m-%d %H:%M (lunch time)\n"))
	elif (now.hour == (statTime + 7) and now.minute <= 5):
		print ("Welcome back")
		f.write(now.strftime("%Y-%m-%d %H:%M (start after lunch)\n"))
	elif (now.hour == (statTime + 7) and now.minute >= 5):
		print ("Hurry up")
		f.write(now.strftime("%Y-%m-%d %H:%M (late)\n"))
	elif (now.hour == (statTime + 9) and now.minute <= 5):
		print ("See you tomorrow")
		f.write(now.strftime("%Y-%m-%d %H:%M (end work)\n"))
	elif now.hour > (statTime + 9):
		print ("Go home !!!")
		f.write(now.strftime("%Y-%m-%d %H:%M (end work + owertimes)\n"))
f.close()