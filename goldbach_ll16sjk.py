# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:02:08 2018

@author: Sam Kettlewell
"""
#Obtain relevant imports
import time
import matplotlib.pyplot as plt
from math import sqrt, floor

'''Note on my computer, the code took approximately 3 seconds to run in total. With the
majority of the time being equally spread (about 1 sec each) on generating the primes,
and verifying the first two conjectures.'''

t_1 = time.time()

'''Conjecture 1 - Goldbach's conjecture states that every even number greater than 4 
is the sum to two odd prime numbers. To investigate this we consider the following
method.

Method - The best solution I can think of is given any even number, generate a list of 
primes s.t. max(prime_list) < even_number then for each prime in prime_list, subtract the
prime from the even number and check whether the difference is prime. If it is, the prime
and the difference are two prime numbers summing to an even number and hence satisfy
Goldbach's conjecture.'''



'''Given a number N, use the sieve of Eratothenes to generate a list of primes upto and
including N''' 
def generate_primes(N):
    prime_list = list(range(2, N+1))
    
    for i in prime_list:
        j=2
        while i*j <= prime_list[-1]:
            if i*j in prime_list:
                prime_list.remove(i*j)
            j += 1
    
    return prime_list

'''Throughout this investiagtion, both prime numbers and odd & even numbers will have
to be generated. These tasks (especially prime generation) will take a significant
amount of time. To remedy this, I generate two lists here: one containing all primes
upto and including N=10000 and another containing all numbers upto and including
N=10000. Whenever I need to access primes or odd or even numbers I can obtain them
much more quickly by taking slices from these lists.'''
global_primes_list = generate_primes(10000)
global_numbers_list = [n for n in range(1,10001)]

#########################################################################
'''First time marker: time required to generate the global lists'''
t_2 = time.time()
print("Primes and Numbers generated.")
print("Time taken to complete (s): " + str(t_2 - t_1))
print("")
#########################################################################

'''Given a number N, this function wil return a list of all 3-tuples: (p,q,r) such that
p=q+r for p even and q & r odd and prime. i.e. satisfying Goldbach's conjecture'''
def goldbach(N):
    list_of_sums = []
    evens_to_test = global_numbers_list[1:N:2] #Slice all the even numbers from global_numbers_list
    primes_list = global_primes_list[0:N] #Slice all primes upto N from global_primes_list
    primes_list.remove(2) #We are only interested in odd primes for this task.

    for even_number in evens_to_test:
        primes_to_test = primes_list[0:even_number]
        #Take a slice of the list so there are less primes to check.
        
        for test_prime in primes_to_test:
            if (even_number - test_prime) in primes_to_test: #Since primes_to_test contains only positive primes
                primes_to_test.remove(even_number - test_prime) #Since addition commutes
                list_of_sums.append((even_number, test_prime, even_number-test_prime))
    
    return list_of_sums
'''This algorithm is of complexity order O(n^2) since a calculation is performed in a
nested loop. This is unfortunate however I have done my best to reduce the calculations
being performed inside the loops to only the absolutely necessary ones.'''

'''Given a number N, this function will return an ordered list of the number of unique
ways each even number upto and inculding N can be written as satisfying either Goldbach
or Lemoine's conjecture.'''
def unique_expressions(N, conjecture):
    
    if conjecture == "goldbach": #Generate all sums upto N
        list_of_sums = goldbach(N) 
    elif conjecture == "lemoine":
        list_of_sums = lemoine(N)
        
    list_of_occurences = [] #Empty arrays to store the sums and ___
    list_of_unique_expressions = []
    
    '''Extract the first element of each 3-tuple representing a unique sum satisfying 
    the relevant conjecture. i.e. for any n which can be expressed k unique ways as the
    sum of two even primes, this list contains n, k times.'''
    for each_sum in list_of_sums:
        list_of_occurences.append(each_sum[0])
    
    '''Simplify the above list into a list containing the k-value: i.e. how many
    occurences of each expression occur.'''
    for each_unique_expression in set(list_of_occurences):
        list_of_unique_expressions.append(list_of_occurences.count(each_unique_expression))
    
    return (list_of_occurences, list_of_unique_expressions)
'''This function calls an O(n^2) function each time it runs so it has order at least
O(n^2). The other parts are O(n) however as there is only a single loop performing
a calculation each time.'''

'''This function, given a range of numbers and a list to check, checks whether each
number in the range occurs in the list at least once. This function will be useful to
test the "every" part of each conjecture as it will quickly verify for us whether or
not every number has been 'hit' at least once by the conjectures.'''
def check_occurences(range_list, check_list):    
    for each_to_check in range_list:
        if each_to_check not in check_list:
            return False
        
    return True


'''Check EVERY even number greater than 4 can be expressed as the sum of two primes'''
N = 800 #Suitable N for time-efficiency vs. suitable number tested
goldbach_list_to_check = unique_expressions(N, "goldbach")
print("Goldbach's conjecture verified upto " + str(N) + ": " + 
      str(check_occurences([x for x in range(6,N,2)], goldbach_list_to_check[0])))

'''Plot a chart of the number of ways each even number can be uniquely expressed as a
sum of two odd primes. Firstly obtain the coordinates in list form.'''
y_coordinates = goldbach_list_to_check[1]
x_coordinates = [2*x for x in range(4, len(y_coordinates)+4)]

'''Label the axes'''
fig, axes_array = plt.subplots(2) #2 charts to plot on the same figure, axarr="axes_array"
axes_array[0].set_title("Goldbach's Conjecture")
axes_array[0].set_xlabel("n")
axes_array[0].set_ylabel("Unique expressions \n of even numbers")

'''Plot the scatter graph'''
axes_array[0].scatter(x_coordinates, y_coordinates, marker = '.')

#########################################################################
'''Second time marker: Time taken to verify goldbach's conjecture'''
t_3 = time.time()
print("Time taken to complete (s): " + str(t_3 - t_2))
print("")
#########################################################################

'''Conjecture 2 - The Emile-Lemoine/Levy's conjecture states that every odd number 
greater than 5 can be expressed as the sum of a prime and twice a prime. We simply 
modify the method used above for Goldbach's conjecture to produce the following 
function.'''

def lemoine(N):
    list_of_sums = [] #Empty array to store the 3-tuple sums
    primes_list = global_primes_list[0:N] #Suitable primes
    double_primes_list = [2*x for x in primes_list[0:len(primes_list)//2]]
    odd_numbers = global_numbers_list[0:N:2]
    
    for each_odd in odd_numbers:
        for each_prime in primes_list[0:each_odd]: 
            if (each_odd - each_prime) in double_primes_list:
                list_of_sums.append((each_odd, each_prime, each_odd-each_prime))
    
    return list_of_sums
'''This function is of complexity order O(n^2) again as it is very similar to the
code used to verify Goldbach's conjecture. As a result I have once again tried to
move as many 'unnecessary' calcualtions outside the loops as possible.'''


'''Note at this point I went back and modified the above, unique_expressions function
as we wish to plot the same type of graph as we did for the Goldbach conjecture but 
with Lemoine sums instead. This is essentially to save me writing the same code out
twice because it's quite a big chunk of it'''

'''Check EVERY odd number greater than 5 can be expressed as the sum of a prime and
twice a prime.'''
#N = 800 #Highly suggested to keep the same N both times for axes! (Can change if you want I suppose)
lemoine_list_to_check = unique_expressions(N, "lemoine")
print("Lemoine's conjecture verified upto " + str(N) + ": " + 
      str(check_occurences([x for x in range(7,N,2)], lemoine_list_to_check[0])))

'''Plot a chart of the number of ways each odd number can be uniquely expressed as the
sum of a prime and twice a prime'''
y_coordinates = lemoine_list_to_check[1]
x_coordinates = [2*x+1 for x in range(3, len(y_coordinates)+3)]

'''Label the axes'''
axes_array[1].set_title("Lemoine's Conjecture")
axes_array[1].set_xlabel("n")
axes_array[1].set_ylabel("Unique expressions \n of odd numbers")

'''Plot the scatter graph'''
axes_array[1].scatter(x_coordinates, y_coordinates, marker = '.')

plt.tight_layout() #Finalse some plotting graphics options

#########################################################################
'''Third time marker: time taken to verify Lemoine's conjecture'''
t_4 = time.time()
print("Time taken to complete (s): " + str(t_4 - t_3))
print("")
#########################################################################

'''Conjecture 3 - This states that every odd composite (non-prime) number can be 
written as the sum of a prime and twice a square.
    
Method - Consider all odd numbers beginning from 3 (since 1 is not composite). Firstly
check if the number is prime, if it is not then for each prime in the list of primes
check whether odd_number-prime is twice a square number. If ONE such example exists,
break out of the loop and increment to the next odd number and try again.'''

'''Given a number N, this function returns a list of composite (non-prime) numbers
upto and including N.'''
def generate_composite_odd_numbers(N):
    odd_prime_list = global_primes_list[1:N]
    odd_numbers = [x for x in global_numbers_list[2:N:2] if x not in odd_prime_list]
    
    return odd_numbers

'''Given a number N, this function tests whether N is twice a square. It does this by
checking if the quantity sqrt(N/2)-int(sqrt(N/2)) has a fractional part. It is only
defined on positive N.'''
def is_double_square(N):
    if N > 0: #If N is negative then it can't be double a square. Return False.
        if sqrt(N/2) - int(sqrt(N/2)) == 0: #If there is no decimal part to N/2 return True
            return True 
    return False

'''This function seeks out the smallest counterexample to the claim "Every odd
composite number can be written as the sum of a prime and twice a square."'''
def goldbach2():
    counter_example = False #Boolean to check whether a counterexample has been found
    odd_number = 1
    
    while counter_example != True:
        odd_number += 2 #Increment
        
        if odd_number not in global_primes_list[0:odd_number]: #If odd_num is composite
            counter_example = True #Assume this current number is the counterexample
            
            for each_prime in global_primes_list[0:odd_number]:
                if is_double_square(odd_number - each_prime) == True:
                    counter_example = False #If one example is found, counter = False
                    break #Immediately quit the loop and try the next odd number.
    
    return odd_number
'''This function is of complexity order O(n^2) due to the prescence of the nested loop.
It is irrelevant however as the counterexample is small enough to be found quickly.
Should the counterexample have been bigger however, a different approach would have
been required.'''

print("Goldbach's first counterexample: " + str(goldbach2())) #Find the smallest counterexample

#########################################################################
'''Fourth time marker: time taken to find the counterexample to Goldbach's second
conjecture.'''
t_5 = time.time()
print("Time taken to complete (s): " + str(t_5 - t_4))
print("")
#########################################################################

'''Continuing with the theme of Prime Number Conjectures we nextly investigate
de Polignac's conjecture.

Conjecture 4 - de Polignac's conjecture states that for any even number n, there are
infinitely many cases of two consecutive prime numbers with difference n.'''
def de_Polignac(N):
    primes_list = global_primes_list[0:N] #Suitable slice of prime list
    consecutive_prime_gaps = [] #Empty array to store the differences
    current_prime_index = 1
    
    '''For all primes in the list, calculate the difference between consecutive primes
    and add this difference to the consecutive_prime_gaps list.'''
    while current_prime_index < len(primes_list):
        difference = primes_list[current_prime_index]-primes_list[current_prime_index-1]
        consecutive_prime_gaps.append(difference)
        current_prime_index += 1
    
    '''Create a list of tuples: (length of prime gap, number of occurences in list), and
    for each prime gap in the consecutive_prime_gaps list, count the number of times
    each prime gap occurs and add it to the prime_gap_count list as an appropriate
    tuple.'''
    prime_gap_count = [(1,1)]
    max_prime_gap = max(consecutive_prime_gaps)
    for each_prime_gap in range(2, max_prime_gap+1, 2):
        prime_gap_count.append((each_prime_gap, consecutive_prime_gaps.count(each_prime_gap)))
    
    return (consecutive_prime_gaps, prime_gap_count)
'''This function is complexity order O(n) (Hooray) since there are no nested loops
involved in calculation here, double the N value and the time taken should also
double.'''

'''Calculate the prime gap count for the whole of the global_primes_list and plot it as
a bar chart. Begin a new figure here as the chart is suitably different'''
prime_gaps = de_Polignac(10000)
x_coordinates = [prime_gaps[1][x][0] for x in range(len(prime_gaps[1]))]
y_coordinates = [prime_gaps[1][x][1] for x in range(len(prime_gaps[1]))]

'''Begin a new figure and label the axes'''
plt.figure(2) #Start a new window to display the bar chart as it is different
plt.title("de Polignac's Conjecture")
plt.xlabel("Prime Gap")
plt.ylabel("Occurences of prime gap")

'''Plot the bar chart'''
plt.bar(x_coordinates, y_coordinates)

#########################################################################
'''Fifth time marker: Time taken to compute and plt the bar chart of prime gaps
for de Polignac's conjecture.'''
t_6 = time.time()
print("de Polignac's conjecture bar chart plotted.")
print("Time taken to complete (s): " + str(t_6 - t_5))
print("")
#########################################################################

'''Further, continuing with prime number conjectures, we nextly investiagte Legendre's
conjecture. 

Conjecture 5 - Legendre's Conjecture states that for every positive integer N, there
exists a prime number between N^2 and (N+1)^2.'''

'''Given a number N, this function will return a boolean indicating whether or not
there exists a prime between N and N+1. Note due to the size of global_primes_list, 
this function can only return a meaningful answer when N <= sqrt(max(global_primes_list))'''
def legendre(N):
    if N >= sqrt(max(global_primes_list)):
        return "global_primes_list contains insufficient primes to verify N."
    
    #List all all numbers between N^2 and (N+1)^2
    square_N_interval = [x for x in range(N**2, ((N+1)**2)+1)]
    
    #For each number in the interval, check if at least one is prime.
    for each_N_integer in square_N_interval:
        if each_N_integer in global_primes_list[0:each_N_integer]:
            return True
    
    return False
'''This code is of complexity order O(n) also in a similar (but more obvious) fashion
to the de_Polignac function.'''

#We must change N here to satisfy N <= sqrt(max(global_primes_list))
N=floor(sqrt(max(global_primes_list))) 
print("Legendre's conjecture verified upto " + str(N) + ": " + 
      str(check_occurences([True for x in range(N)], [legendre(x+1) for x in range(N)])))

#########################################################################
'''Sixth time marker: Time taken to verify the Legendre conjecture'''
t_7 = time.time()
print("Time taken to complete (s): " + str(t_7 - t_6))
print("")
#########################################################################

'''Finally, we investigate Andrica's conjecture.

Conjecture 6 - Andrica's conjecture states that the difference between the square roots
of consecutive prime numbers is less than 1.'''

'''Since we have already calculated the prime gaps in the de_Polignac function we can
utilise this. The conjecture is equavalent to saying that the n-th prime gap is less
than 2*nth_prime + 1. We modify the de_Polignac function to return the list of prime
gaps also and then we can access it here.'''

'''For each prime gap in the list prime_gaps[0] this function tests whether the gap
satisfies the equiavlent condition to Andrica's conjecture: the n-th prime gap is less
than 2*nth_prime + 1.'''
def andrica(gap_index): 
    prime_g = prime_gaps[0] #Rename the list for readability
    
    if prime_g[gap_index] < 2*global_primes_list[gap_index] + 1:
        return True #If it meets the condition, return True.
    
    return False
'''This code is said to be executed in 'constant time': i.e. O(1). This is because
there are no loops involved whatsoever, the function andrica simply checks (for ONE
given input) whether the input satisfies a particular condition and returns True or
False depending. This makes it the fastest function in the code so far.'''

'''We then verify it using the check_occurrences function in a similar fashion to that
of Legendre's conjecture.'''
N=1220 #Suitable N for the number of primes we have.
print("Andrica's conjecture verified upto " + str(N) + ": " + 
      str(check_occurences([True for x in range(N)], [andrica(x+1) for x in range(N)])))

#########################################################################
'''Seventh time marker: Time taken to verify the Andrica conjecture'''
t_8 = time.time()
print("Time taken to complete (s): " + str(t_8 - t_7))
print("")
#########################################################################

print("Total time taken (s): " + str(t_8-t_1)) #Print how long the whole program has taken to run in secs