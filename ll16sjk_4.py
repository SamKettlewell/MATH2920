# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:00:31 2018

@author: Sam Kettlewell
"""
from math import floor, sqrt, pi, e

#Exercise 4.A - Continued Fraction representation of a real x
def contFrac(x, i):
    contFracList = []   
    
    while i > 0:
        contFracList.append(floor(x))
        x = 1/(x-floor(x))
        i -= 1
    
    return contFracList

for eachConstant in [sqrt(2), sqrt(3), sqrt(7), pi, e]:
    print(contFrac(eachConstant, 20))

print(contFrac(sqrt(2), 30)) #Inexact due to sqrt(2) being itself inexact.

#contFrac(sqrt(2), 20) = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#contFrac(sqrt(3), 20) = [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
#contFrac(sqrt(7), 20) = [2, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1]
#contFrac(pi, 20) = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 3, 3, 23, 1, 1, 7, 4]
#contFrac(e, 20) = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1]

#Suppose x>0 then the fractional part of x, x-floor(x), is smaller than x and hence
#1/(x-floor(x)) > 0. Hence the fractional part of this is smaller than 1/(x-floor(x)) and ... 

#Exercise 4.B - Continued fraction representation of a rational x
def ratContFrac(num, den):
    contFracList = []
    
    while den > 0:
        contFracList.append(num//den)
        num = num%den
        num, den = den, num #Surely the order you do this matters?
    
    return contFracList

#ratContFrac(97, 61) = [1, 1, 1, 2, 3, 1, 2]
#ratContFrac(1066, 1012) = [1, 18, 1, 2, 1, 6]
#ratContFrac(123456789, 987654321) = [0, 8, 13717421]
    
#I'm not sure - I see no reason why it shouldn't be exact just because x<0. Please advise.
    
#Exercise 4.C - Nth partial convergent of a continued fraction
def partialConv(a, k):
    contFractionList = contFrac(a, k)
    den = contFractionList[k-1]
    num = 1
    
    for j in range(2, k+1): #since by defintion the first partial convergent is the zeroth
        num=contFractionList[k-j]*den+num
        den, num = num, den
        
    return den, num
        
#Function to make the tuples returned from the partialConv function into 'nice' fractions.
def fracToString(fracTuple):
    return str(fracTuple[0]) + "/" + str(fracTuple[1])


print([fracToString(partialConv(sqrt(2), i)) for i in range(1, 6)])
print([fracToString(partialConv(pi, i)) for i in range(1, 6)])

for eachConv in [partialConv(sqrt(5), i) for i in range(1, 6)]:
    if abs(eachConv[0]/eachConv[1] - sqrt(5)) < (0.001/100):
        print(fracToString(eachConv))
        break
    
#The first five partial convergents to sqrt(2) are ['1/1', '3/2', '7/5', '17/12', '41/29']
#The closest approximation to pi with denominator at most 113 is 355/113.
#The first partial convergent of sqrt(5) within 0.001% accuracy is 682/305.