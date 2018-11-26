# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:07:07 2018

@author: Sam Kettlewell
"""
#Obtain relevant imports and define relevant functions for later use.
from time import perf_counter
from random import randint, shuffle
from matplotlib import pyplot as plt

##FUNCTIONS##
#Exercise 8 (1) - Function implementing selection sort. Complexity order O(n^2)
def selectionsort(sortingList):
    sortedList = []
    
    while len(sortingList) > 0:
        smallestCandidate = sortingList[0] #Guess the smallest number to be the first one
        
        for x in sortingList: #for each number in the list
            if x < smallestCandidate: #if it's smaller than the smallest
                smallestCandidate = x #make it the new smallest       
        sortedList.append(smallestCandidate) #add it to the sorted list
        sortingList.remove(smallestCandidate) #remove it from the unsorted list
    return sortedList

#Exercise 8 (3) - Function to implement the bubblesort algorithm. Complexity order O(n^2)
def bubblesort(sortingList):
    for i in range(len(sortingList)-1, 0, -1): #Count down from n-1
        for j in range(i):
            if sortingList[j] > sortingList[j+1]: #If the elements are in the wrong order
                sortingList[j+1], sortingList[j] = sortingList[j], sortingList[j+1] #swap them
    return sortingList

#Exercise 8 (5) - Function to implement the mergesort algorithm. O(nlogn)
def mergesort(sortingList):
    if len(sortingList) <= 1: #if list is one element long, then it is sorted
        return sortingList

    m = len(sortingList) // 2 #Halve the legnth of the list (what happens if odd?)
    l = mergesort(sortingList[:m]) #Recursively call the function on the half lists
    r = mergesort(sortingList[m:])

    sortedList = []
    i = j = 0
    while (len(sortedList)<len(r)+len(l)):
        if l[i] < r[j]:
            sortedList.append(l[i])
            i = i+1
        else:
            sortedList.append(r[j])
            j = j+1
        if i == len(l) or j == len(r):
            sortedList.extend(l[i:] or r[j:])
            break
    return sortedList

#Exercise 8 (8) - Function to implement the function I have named 'shufflesort'. It checks
#whether the list is in order, if it is, it returns the list. Otherwise, randomly shuffle
#the list and check again. I chose to do this using iteration rather than recursion due to
#constantly reaching the maximum recursion depth.
def shufflesort(sortingList):
    sortedList = sorted(sortingList) #Inbuilt Python method to sort the list.

    while True: #Just keep going until Python 'breaks' out of the loop by returning the list
        if sortingList == sortedList: #If the list is the same as the sorted list: i.e. sorted
            return sortingList #Return it
        shuffle(sortingList) #If not, randomly shuffle it

#The function below returns the time taken for a 'sortingAlgorithm' (specified by user)
#to sort a list of random integers of length 2^i (for i=1,2,...,10). We make use of a
#function to avoid redundant code because in later questions, we are
#going to require the list of times taken for different sorting algorithms.
def clockSort(sortingAlgorithm, listLength):
    randomList = [] #This will be the list of random integers of length 2^i
    y = [] #This will be the list of times taken to sort each list.

    for i in range(1,listLength): #change to 10?
        for listLength in range((2**i)+1):
            randomList.append(randint(1,(2**i)+1)) #check it starts at 1
                
        #This conditional differentiates between the different sorting algorithms and
        #produces a list of times specific to one algorithm. The t_start and t_end
        #counters are in the if statements to make the measurements as accurate as
        #possible.
        if sortingAlgorithm == "selectionsort":
            t_start = perf_counter() #Begin the timer
            selectionsort(randomList) #Sort the list using the specific algorithm
            t_end = perf_counter() #End the timer
        elif sortingAlgorithm == "bubblesort":
            t_start = perf_counter()
            bubblesort(randomList)
            t_end = perf_counter()
        elif sortingAlgorithm == "mergesort":
            t_start = perf_counter()
            mergesort(randomList)
            t_end = perf_counter()
        elif sortingAlgorithm == "pythonsort":
            t_start = perf_counter()
            randomList.sort()
            t_end = perf_counter()
        elif sortingAlgorithm == "shufflesort":
            t_start = perf_counter()
            shufflesort(randomList)
            t_end = perf_counter()

        t_i = t_end-t_start #Calculate the time difference (i.e. time to sort the list)
        print(sortingAlgorithm + ": t(" + str(i) + ") = " + str(t_i)) #Print the times to the console
        y.append(t_i) #Add the time to the end of the list.
        
    return y #Return the list of ordered times


##EXERCISES##
#Exercise 8 (1) - Create a list of times to sort the ten lists using 'selectionsort'
#Print the results to the console.
selectionSortTimes = clockSort("selectionsort", 11)
    
#Exercise 8 (2) - Plot the times found in (1) against 2^i on a loglog plot (suitable scale)
#The graph confirms that selection sort is O(n^2) since the line curves slightly upwards
#as the number of elements increases.
plt.loglog([2**x for x in range(1,11)], selectionSortTimes, label="Selection Sort")
plt.savefig("ll16sjk_selection.png")

#Exercise 8 (3) - bubblesort function defined above. Had to be above 'clockSort'

#Exercise 8 (4) - Find and plot the times for bubblesort to sort the lists of length 2^i.
#Use the same axes.
bubbleSortTimes = clockSort("bubblesort", 11)
plt.loglog([2**x for x in range(1,11)], bubbleSortTimes, label = "Bubble Sort")
plt.savefig("ll16sjk_bubble.png")

#Exercise 8 (5) - (The mergesort function has been implemented above). Find and plot the
#times for mergesort to sort the lists of length 2^i. Plot them on the same log-log axes.
mergeSortTimes = clockSort("mergesort", 11)
plt.loglog([2**x for x in range(1,11)], mergeSortTimes, label = "Merge Sort")
plt.savefig("ll16sjk_merge.png")

#Exercise 8 (6) - Use Python's inbuilt sort function to sort the list. Measure the time
#taken for it to do this and add a plot of the time against 2^i to the same axes for
#comparison. 
pythonSortTimes = clockSort("pythonsort", 11)
plt.loglog([2**x for x in range(1,11)], pythonSortTimes, label = "Python Sort")

#We see Python's inbuilt sorting algorithm is faster than any of the previous sorting
#algorithms we have encountered (in particular mergesort) since at any point on the curve,
#the time-value for the Python sorting algorithm is smaller than that of any other.

#Exercise 8 (7) - Upgraded version of bubblesort. Counts the number of swaps made each
#time the list is iterated over, if the number of swaps is 0 after the first poass
#then the list is already in order so there is no need to continue iterating. Simply
#return the list.
def bubblesort2(sortingList):
    for i in range(len(sortingList)-1, 0, -1):
        swaps = 0 #Start a counter for the number of swaps performed by the algorithm.
        #The swaps variable should be defined here because then it checks to see whether
        #the list is sorted at 'any' pass, not just whether the list is originally sorted.
        
        for j in range(i):
            if sortingList[j] > sortingList[j+1]: #If two elements are in the wrong order
                swaps += 1 #Increment the counter
                sortingList[j+1], sortingList[j] = sortingList[j], sortingList[j+1] #swap them
        if swaps == 0: #If, after one pass, the number of swaps counted is still 0 (no swaps made)
            return sortingList #The list is already in order so return it.
    return sortingList #Otherwise continue iterating over the list and making swaps until sorted

#Generate 10 sorted lists of length 2^i for i=1,2,...,10 - Collapsed into 1 line for brevity
sortedLists = [[j for j in range(1,(2**i)+1)] for i in range(1,11)]
bubblesort2_y = [] #List to contain times taken to sort lists by bubblesort2

#Note we have to run this code seperately from the clockSort function because clockSort
#has no means to generate presorted lists. Measure the time taken for bubblesort2 to sort
#each sorted list.
for eachList in sortedLists:
    t_start = perf_counter() #Start the timer
    bubblesort2(eachList) #Bubblesort the lists
    t_end = perf_counter() #Stop the timer
    bubblesort2_y.append(t_end-t_start) #Append the time difference to bubblesort2_y

#Add a plot of time taken for bubblesort2 to act on sorted lists against 2^i for list length i.
plt.loglog([2**x for x in range(1,11)], bubblesort2_y, label = "Bubble Sort Upgrade")

#We see the graph confirms O(n) behaviour for sorted lists because beyond approx. x=10
#the curve is linear.

#Exercise 8 (8) - The shufflesort algorithm has been implemented above (Had to be above
#clockSort).
shuffleSortTimes = clockSort("shufflesort", 3) #Limit to i=2 so the code doesn't take forever.
plt.loglog([2**x for x in range(1,3)], shuffleSortTimes, label = "Shuffle Sort") #Add the plot

#This algorithm has complexity O(n!). This is visible by the rapidly increasing graph
#(and also intrinsically by Python's inability to exceed length 2**3 in a few seconds).
#We can justify this mathematically as follows: with each random shuffle of a list of
#length n, Python chooses -randomly- what will be the first element from n elements. It
#then chooses the second from (n-1) and the third from (n-2) and ... and the last from 1.
#So the time complexity of this algorithm is n(n-1)(n-2)...1 = n!.

#Modify some properties of the graph to make it more readable.
plt.legend(loc='upper left', ncol=2)
plt.show()