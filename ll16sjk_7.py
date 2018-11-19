# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:09:56 2018

@author: Sam Kettlewell
"""
##PREAMBLE - Import or create all relevant functions before proceeding with exercise##
#Acquire relevant imports.
import matplotlib.pyplot as plt
from random import randint
from math import sqrt, floor
from time import time

#Function to return the standard deviation of a list of real numbers.
def stdev(sample):
    n = len(sample)
    sampleMean = sum(sample)/n
    sampleSquared = [x**2 for x in sample]
    
    return sqrt(1/(n-1) * (sum(sampleSquared) - n*sampleMean**2))

#Function to scatterplot each random sample to visually check randomness of samples.
def checkRandom(randomSample, label):
    x = randomSample
    
    y= x[:]
    y.append(x[0])
    del(y[0])

    plt.scatter(x, y, marker='.', label=label)

##Exercise 7.A (1)##
#Lagged Fibonnaci Generator
#SEED - [37495, 1740926, 128, 47298564, 1092, 1111111, 463909827, 1234567890, 987654321, 1657387]
def lagFib(j, k, L):
    m = 2**32
    S = [37495, 1740926, 128, 47298564, 1092, 1111111, 463909827, 1234567890, 987654321, 1657387]

#####TIME GENERATOR#####
#Is there a better way to do this? When I do it without the if, the computer is fast
#enough such that all the times in the list are the same.
    
#    while len(S) <= k:
#        t = m*(time() - floor(time()))
#        if t not in S:
#            S.append(t)
#            print(S)
    
    for n in range(len(S), L):
        S.append((S[n-j] + S[n-k]) % m)
    
    return S

##Exercise 7.A (2)##
#Generate L = 2000 pseudorandom numbers in the range [0, 2^32) with (j,k,m) = (7, 10, 2^32).
empiricalRandomList = lagFib(7, 10, 2000)

#Plot x_i against x_(i-1) as a scatterplot using the checkRandom function.
checkRandom(lagFib(7, 10, 2000), "Lagged Fibonacci Generator")

##Exercise 7.A (3)##
#Generate L = 2000 pseudorandom numbers in the range [0, 2^32) with the inbuilt Python
#'random' module.
theoreticalRandomList = [randint(0, 2**32) for r in range(2000)]

#Plot z_i against z_(i-1) as a scatterplot using the checkRandom function.
checkRandom(theoreticalRandomList, "Python Inbuilt Generator")

##Exercise 7.A (4)##
#Compare the mean and standard deviation of the random numbers x_i to the random numbers z_i
print("Empirical Mean: " + str(sum(empiricalRandomList)/2000))
print("Empirical Standard Deviation: " + str(stdev(empiricalRandomList)))

print("") #newline#

print("Theoretical Mean: " + str(sum(theoreticalRandomList)/2000))
print("Theoretical Standard Deviation: " + str(stdev(theoreticalRandomList)))

#Modify some properties of the plot to make the chart more readable.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1, ncol=2, mode="expand", borderaxespad=0.)
plt.show()