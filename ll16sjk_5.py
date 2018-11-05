# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:04:18 2018

@author: Sam Kettlewell
"""
from math import sin, cos, pi, sqrt, atan
#Exercise 5.A - Write functions to perform the following tasks

#Given an integer x, return x^3.
def cube(x):
    return x**3

#Given two real numbers x and y, return their sum and difference as a tuple.
def sumAndDif(x, y):
    return (x+y, abs(x-y)) #Take the modulus to remove any signs and leave only the 'difference'

#Given any real x, return sin(x)^2 + cos(x)^2.
def trigPythag(x):
    return 1 #Since sin(x)^2 + cos(x)^2 is identically 1.

#Given any integer n, return the first n fibonacci numbers.
#F(1) = 1, F(2) = 1, F(n)=F(n-1)+F(n-2)
def fibonacci(n):
    fibList = [1, 1] #Define a list containing the first two fibonacci numbers.
    for f in range(2, n):
        fibList.append(fibList[f-2] + fibList[f-1]) #Sum the previous two terms in the list. 
    return fibList

#Given r and theta, Converts a given polar coordinate into its Cartesian equivalent.
#Return it as a tuple (x,y).
def polarToCartesian(r, theta):
    return (r*cos(theta), r*sin(theta))

#Given x and y, convert a given Cartesian coordinate into its polar equivalent.
def cartesianToPolar(x, y):
    r = sqrt(x**2 + y**2) #Using Pythagoras' Theorem to find the length of the line segment.
    
    #Conditional 1 - If the point lies on the y-axis (x=0), then y/x won't be defined so we
    #must set up each theta as a special case: pi/2 if it's on the positive y-axis and
    #3pi/2 if it's on the negative y-axis. The angle is undefined at the origin.
    #If x is non-zero, calculate basetheta as normal and move to conditional 2.
    if x == 0: #if x isn't 0, don't check any further for efficiency
        if y < 0: 
            basetheta = 3*pi/2
        elif y > 0: 
            basetheta = pi/2
        elif y == 0: 
            return 'undefined'
    else:
        basetheta = atan(y/x) #Basetheta is the standard value of theta. It is correct for the first quadrant.
        
    #Conditional 2 - If x=0 or x>0 & y>0 this won't run, otherwise it will modify the value
    #of basetheta so it lies in the range [0, 2pi) and is correct w.r.t the quadrant it's in. 
    if x < 0:
        basetheta += pi
    elif x > 0 and y < 0:
        basetheta += 2*pi
    
    return (r, basetheta)

#Exercise 5.B - Evaluating Polynomials with Functions
    
#Function to evaluate polynomials. Users are more likely to input coefficients reading
#left to right but the function reads from the smallest power of x which is generally from
#right to left. As such, we reverse the list to begin with.
#i.e. 3x^2+2x+4 corresponds to [3,2,4] not [4,2,3]. This will continue for all the functions.

#A function to eavluate polynomials the 'traditional' way: raise x0 to the power of the
#exponent and multiply by the relevant coefficient. Sum each term.
def poly(x0, coeffs):
    coeffs.reverse()
    sumtotal = 0
    for n in range(len(coeffs)):
        sumtotal += coeffs[n] * (x0 ** n)
    return sumtotal

#A(x) = x^3+3x+2; A(6) = 236
print(poly(6, [1,0,3,2])) #This is exact because all calculations involve integers.

#B(x) = 2-x^2; B(sqrt(2)) = -4.440892098500626e-16
print(poly(sqrt(2), [-1, 0, 2])) #This is not exact because sqrt(2) is not perfectly accurate.


#A function to implement Horner's method for evaluating polynomials
def horner(x0, coeffs):
    sumtotal = 0
    for n in coeffs:
        sumtotal = x0*sumtotal + n
    return sumtotal

#A function to extend Horner's method to find the derivative of a polynomial.
def derivHorner(x0, coeffs):
    sumtotal, deriv = 0, 0
    for n in coeffs:
        deriv = x0*deriv + sumtotal
        sumtotal = x0*sumtotal + n
    return deriv

#P(x) = 7x^5-4x^3+x^2.
print(horner(1, [7, 0, -4, 1, 0, 0])) #P(1) = 4
print(derivHorner(1, [7, 0, -4, 1, 0, 0])) #P'(1) = 25
print(horner(pi, [7, 0, -4, 1, 0, 0])) #P(pi) = 2097.98...
print(derivHorner(pi, [7, 0, -4, 1, 0, 0])) #P'(pi) = 3297.17...

#We use the Maclaurin series of sin(x) at x=pi/4 to obtain an approximation of 1/sqrt(2)
print(horner(pi/4, [-1/5040, 0, 1/120, 0, -1/6, 0, 1, 0])) #1/sqrt(2) = 0.7071064695751781...