# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:01:00 2018

@author: Sam Kettlewell
"""
#Obtain relevant imports
from random import randint
import matplotlib.pyplot as plt
from box import boxcounting

#Exerises 9A - (1)
#Function to generate serpinski fractals
def generate_sierpinski():
    iterations = 50000 #more iterations -> more detail
    
    x = [0.0, 1.0, 0.5, 0.2] #plot start points of the triange
    y = [0.0, 0.0, 0.8, 0.3]
    r = 0.5 #distance to move each iteration
    
    for i in range(iterations):
        p = randint(0,2)
        x.append(x[-1]*(1-r)+x[p]*r) #add the points to the lists
        y.append(y[-1]*(1-r)+y[p]*r)
    
    plt.scatter(x, y, s=0.1) #plot and save results
    plt.savefig("ChaosGame.png")
    
    return(x,y)

sierpinski_fractal = generate_sierpinski() #Geenerate and plot a sierpinski triangle.

#Exercises 9A - (2) - Boxcounting function imported above

#Exercises 9A - (3)
#We estimate the box counting dimension by suitably shrinking the epsilon value.
print(boxcounting(sierpinski_fractal[0], sierpinski_fractal[1], 0.002)[2])

#Exercises 9A - (4)
boxNumbers = [] #Lists to contain the log(N(E)) and log(1/E)
epsilonConstants = []

r=50 #Loop to generate the epsilon points
for epsilon in [(1/r)*(x+1) for x in range(r-1)]:
    epsilonConstants.append(boxcounting(sierpinski_fractal[0], sierpinski_fractal[1], epsilon)[0])
    boxNumbers.append(boxcounting(sierpinski_fractal[0], sierpinski_fractal[1], epsilon)[1])
    
plt.plot(epsilonConstants, boxNumbers) #plot the line
#From this plot we see the gradient is approximately 6.5/4=1.63 which is reasonably close to
#the box counting dimension log(3)/log(2).

#Exercises 9A - (5) - This could be made more accurate by increasing the r-value and plotting
#more points. This can't be done for efficiency reasons however.