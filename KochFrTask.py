#!/usr/bin/env python3
from turtle import *

def stringInversion(s):
	tempStr = ''
	for i in range(0,len(s)):
		if( s[i] == '0'):
			tempStr+='1'
		else:
			tempStr+='0'
		 
	
	return tempStr

def doOnePeriod(s):
	s+=stringInversion(s)
	return(s)

numberOfIterations = int(input("Please, enter a number between 1 and 10"))
str = '0'
for i in range( 0, numberOfIterations*2 + 1 ):
	str = doOnePeriod(str)



for i in range( 0, len(str) ):
	if (str[i] == '0'):
		right(180)
	elif(str[i] == '1'):
		forward(10)
		right(60)
done()

