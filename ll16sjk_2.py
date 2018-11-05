# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:08:57 2018

@author: Sam Kettlewell
"""
from math import log, pi
#Exercise 2.A - Euclid's Algorithm
#By integer division. We define it as a function ready for repeated use.
def gcd(a, b):
    while b > 0:
        a, b = b, a%b #Set a to become b and b to become the remainder of a/b.
    return a

print(gcd(105, 24))
print(gcd(6024, 1284))
print(gcd(98777, 12945))

#gcd(105, 24) = 3
#gcd(6024, 1284) = 12
#gcd(98777, 12945) = 1


#Exercise 2.B - Extended Euclid's Algorithm
#This algorithm prints the values (a, xprev, yprev) where a is the gcd and xprev, yprev
#are the vaues satisfying Bezout's identity.
a,b = 105, 24
x,xprev,y,yprev = 0,1,1,0

while b > 0:
    q = a//b
    a, b = b, a%b
    x, xprev = xprev - q * x, x
    y, yprev = yprev - q * y, y
    
print(a, xprev, yprev)

#Exercise 2.C - Counting Steps Algorithm
#Define it as a function this time for repeated use.
def countingEuclid(a, b):
    count = 0
    x,xprev,y,yprev = 0,1,1,0
    a_copy = a #This copy of the variable a is required since the loop changes the value of a.
    
    while b > 0:
        q = a//b
        a, b = b, a%b
        x, xprev = xprev - q * x, x
        y, yprev = yprev - q * y, y
        count += 1
    
    print("Steps Taken: " + str(count))
    print("Approx. maximum steps taken: " + str(5*log(a_copy, 10)))
    print("Approx. average no. of steps taken: " + str(12*log(2)*log(a_copy)/pi**2))
    
#The pair of integers (18,5) takes 4 steps to reach the gcd. This is higher than the expected 2.
#The pair of integers (35, 5) takes 1 step to reach the gcd. This is lower than the expected 3.
countingEuclid(105, 24)
countingEuclid(18, 5)
countingEuclid(35, 5)

#From these results it is clear to see that the number of steps roughly attains the maximum
#for consective Fibonacci numbers.
countingEuclid(34, 55)
countingEuclid(55, 89)
countingEuclid(89, 144)