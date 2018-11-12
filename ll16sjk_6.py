# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:07:33 2018

@author: Sam Kettlewell
"""
import matplotlib.pyplot as plt
import numpy as np

#Exercise 6.A - The Collatz Conjecture
#A function to return the collatz sequence from startpoint n.
def collatz(n):
    collatz = []
    
    while n != 1:
        collatz.append(n)
        
        if n%2 == 0:
            n = n//2 #n will always be even so use // to keep the list int
        else:
            n = 3*n+1
            
    collatz.append(1) #add 1 to the list
    return collatz

#Find the collatz sequence with startpoint n where n=12, n=9, n=27
print(collatz(12)) #[12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
print(collatz(9)) #[9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
print(collatz(27)) #[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]

#A function to count the steps of the the collatz function before 1 is reached
def s(n):
    count = 0 #Instead of appending to a list, every step, add one to count.
    while n != 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        count += 1
    return count

#A function to count the steps required for the collatz function to reach one
print(s(123)) #46 steps
print(s(901)) #54 steps
print(s(63728127)) #949 steps
    
#Plot a graph of s(n) against n for 1<=n<=1000. Use circles for markers.
x = np.arange(1,1001)
sx = [s(n) for n in x]
plt.plot(x, sx, marker='o', label='Steps')

#Work out what percentage of initial values have the property s(n) < n/10
c = 0
for n in x:
    if sx[n-1] < n/10:
        c+=1 #Increment this variable if n satisfies s(n) < n/10
print(c*100/len(sx)) #percentag of values = 44.3%

#Plot a graph of the maximum value attained in the collatz sequence of n for 1<=n<=1000
mx = [max(collatz(n)) for n in x] #Generate a list containing the maximum number from each collatz sequnce
plt.plot(x, mx) #The standard plot shows most attain roughly the same maximum but it is hard to tell what this is since it is obscured by one or two massive peaks
plt.semilogy(x, mx, label = 'Max value attained') #This log-y-axis plot makes it clearer since it reduces the effect of the one or two sharp peaks.
plt.legend(loc='upper left')