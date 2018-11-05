# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:03:33 2018

@author: Sam Kettlewell
"""

#Exercise 3.A - Write functions to perform the following tasks

#1) Take x and return x cubed. This can also cube floats, complex numbers and even booleans!
def cube(x):
    return x**3

#2) Takes a pair of integers x and y and returns their mean.
def mean(x, y):
    return (x+y)/2

#3) Takes three integers and checks if they are a Pythagorean triple.
def pythagTriple(a, b, c):
    return(a**2 + b**2 == c**2)

#4) Takes a list of integers and returns their mean    
def meanList(integerList):
    return sum(integerList)/len(integerList)

#5) Takes a pair of positive integers and returns their greatest common divisor
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

#6) Takes a decimal integer and returns a list representing it's binary equivalent
def decToBin(x):
    binaryRep = []
    while x>0:
        binaryRep.append(x%2)
        x = x//2
    binaryRep.reverse()
    return binaryRep

#7) Takes a list representing a binary number and converts it into a decimal integer
def binToDec(b):
    decimal = 0
    b.reverse()
    for i in range(len(b)):
        decimal += 2**i * b[i]
    return decimal

#8) Takes any date in history and returns the day of the week. Using Zeller's congruence
#Note with this algorithm Jan/Feb are counted as months 13 & 14 of the previous year.
def dayOfWeek(date, month, year):
    #Define a dictionary to relate the numbers to the relevant days for Zeller's algorithm
    dayConversion = {0 : "Saturday",
                     1 : "Sunday",
                     2 : "Monday",
                     3 : "Tuesday",
                     4 : "Wednesday",
                     5 : "Thursday",
                     6 : "Friday"}
    
    #This seems an ugly way to deal with it but it works.
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1
        
    Y = year % 100
    C = year//100
    
    return dayConversion[(date + ((13*(month+1))//5) + Y + (Y//4) + (C//4) -2*C) % 7]

#Exercise 3.B - The Sieve of Eratosthenes
#How do I make this more efficient? Use mod? Save any lists produced already?
def eratosthenes(n):
    primeList = list(range(2, n+1))
    
    for i in primeList:
        j=2
        while i*j <= primeList[-1]:
            if i*j in primeList:
                primeList.remove(i*j)
            j += 1
    
    return primeList

'''Suppose we have a list containing at least 100 prime numbers, then the first element 
of this list will be 2, that is list[0]=2=(1st Prime) so we need to find list[99].

For the last part of this question we wil need primes up to 30,000. We can calculate
the list of primes up to 30,000 once, store it in a variable and access this variable
to find the 100th and 2000th prime also. This will save Python having to compute the list
3 times.

For the last part of the question, eratosthenes(3000) is fairly quick so we
compute that manually rather than searching through the list for an index corresponding
to the prime nearest to 3,000.'''
primeList = eratosthenes(30000)
print(primeList[99]) #The 100th Prime is 541.
print(primeList[1999]) #The 2000th prime is 17389.
print(len(primeList)-len(eratosthenes(3000))) #There are 2815 primes in between 30000 and 3000.


#Exercise 3.C - The Sieve of Sundaram
def sundaram(n):
    primeList = [x for x in range(1,n+1)] #List containing all numbers from 1 to n
    
    j = 1
    while j <= n:
        i=1
        while i <= j:
            s = i+j+2*i*j #Save this from being calculated twice over
            if s in primeList:
                primeList.remove(s)
            i += 1
        j += 1
    return [2*x+1 for x in primeList] #note this excludes 2.

#Generate a list of primes upto 100 using both sieves. Remove 2 from the erato list and then
#compare them to check both work.
modifiedErato = eratosthenes(100)
modifiedErato.remove(2)

print(modifiedErato == sundaram(49)) #Returns true.