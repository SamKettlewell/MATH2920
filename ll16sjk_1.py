# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:41:31 2018

@author: Sam Kettlewell
"""
#Import relevant functions from math module.
from math import floor

#Define a dictionary to relate the numbers to the relevant days for Zeller's algorithm
dayConversion = {0 : "Saturday",
                 1 : "Sunday",
                 2 : "Monday",
                 3 : "Tuesday",
                 4 : "Wednesday",
                 5 : "Thursday",
                 6 : "Friday"}

#Exercise 1.A
#Begin by coding Gauss's Easter Sunday Algorithm - As a function for repeated use
def easterDate(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    
    #The (d+e) portion will determine whether Easter Sunday falls in March or April.
    if (d+e) > 9: #Should this be >= ?
        return str(d+e-9) + " April"
    else:
        return str(22+d+e) + " March"
    
#Next code the Zeller Congruence Algorithm - As a function for repeated use
#This algorithm counts the months January and February as months 13 and 14 of the previous year
#Fortunately none of the dates the question asks for are in Jan or Feb so this doesn't matter :D
#Q: How could I adapt this to make it handle Jan and Feb as months 1 & 2 of the same year?
def zeller(date, month, year):
    Y = year % 100
    C = floor(year/100)
    
    return dayConversion[(date + floor((13*(month+1))/5) + Y + floor(Y/4) +floor(C/4) -2*C) % 7]


print(easterDate(2034))
print(zeller(25, 12, 2018)) #Christmas day is the 25th September
print(zeller(1, 8, 2019)) #Yorkshire Day is the 1st August
print(zeller(26, 12, 1791)) #Charles Babbage was born on the 21st December 1791

#Exercise 1.B
print(list(range(1, 101, 2))) #Create a list starting at 1 and counting up to 100 in 2's
print(list(range(2, 101, 2))) #Create a list starting at 2 and counting up to 100 in 2's

a = list(range(70, 1030, 3))
print(a[2]) #The third element is at index 2 since Python begins counting from 0.

b = list(range(-41, 10))
print(b[-2])

c = 10*a + 5*b
middleElementIndex = (len(c)-1)//2 #Locate the index of the middle element of the list.
print(c[middleElementIndex])
    
x = [1, 3, 5]
y = [2, 4, 6]

vectorSum = [x[0] + y[0], x[1] + y[1], x[2] + y[2]]
print(vectorSum)

dotProduct = (x[0] * y[0]) + (x[1] * y[1]) + (x[2] * y[2]) #The brackets are for readability
print(dotProduct)

crossProduct = [x[1]*y[2]-y[1]*x[2], x[2]*y[0]-y[2]*x[0], x[0]*y[1]-y[0]*x[1]] #Using the standard 'definition' of cross product
print(crossProduct)