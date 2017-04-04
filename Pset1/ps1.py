# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 00:56:16 2017

@author: Priyatham
"""

def load_file(filename):
    cow_dict = dict()
    f = open(filename, 'r')
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

filename = "ps1_cow_data.txt"
cows = load_file(filename)


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    
    # THERE IS NO POINT IN SORTING A DICTIONARY  
    weights = sorted(cows.values(), reverse = True)
    weights_copy = weights[:]
    
    for item in weights:
        if item > limit:
            weights_copy.remove(item)
    
    weights = weights_copy[:]
    
    answer = []
            
    while len(weights_copy) > 0:
        trip = []
        w = 0
        weights = weights_copy[:]
        
        for i in range(len(weights)):
            if (w + weights[i]) <= limit:
                w += weights[i]
                trip.append(weights[i])
                weights_copy.remove(weights[i])
        answer.append(trip)
    
    
    cows_copy = cows.copy()
    
    def get_cow(cdict, val):
        for k,v in cdict.items():
            if val == v:
                cow = k
                del cdict[k]
                break
        return cow
            
    for trip in answer:
        for i in range(len(trip)):
            trip[i] = get_cow(cows_copy, trip[i])
    
    return answer



from ps1_partition import get_partitions

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.
    
    The brute force heuristic should follow the following method:
    1) Enumerate all possible combinations of trips the cows can take
    2) Return the list of trips which has the minimum number of trips and that doesn't break the constraint
    
    Parameters:
    cows - a dictionary of name (string), weight (float) pairs
    limit - weight limit of the spaceship
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    comb = []
    for partition in get_partitions(cows.keys()):
        comb.append(partition)
        
    z = []
    
    for i in range(len(comb)):
        a = []        
        for j in range(len(comb[i])):
            b = []
            for k in comb[i][j]:
                b.append(cows[k])
            if sum(b) > limit:
                break
            a.append(comb[i][j])
        
        if len(a) == len(comb[i]):
            z.append(a)
            
    num_trips = []
    for t_list in z:
        num_trips.append(len(t_list))
    
    for trips_list in z:
        if len(trips_list) == min(num_trips):
            return trips_list
            

import time

def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    greedy_t1 = time.time()
    greedy_trips = len(greedy_cow_transport(cows, 10))
    greedy_t2 = time.time()
    
    brute_t1 = time.time()
    brute_trips = len(brute_force_cow_transport(cows, 10))
    brute_t2 = time.time()
    
    print("Time taken for greedy approach is:", greedy_t2 - greedy_t1, "seconds for", greedy_trips, "trips")
    
    print("Time taken for brute force approach is:", brute_t2 - brute_t1, "seconds for", brute_trips, "trips")  


# Implementation

limit = 10
greedy_cow_transport(cows, limit)
brute_force_cow_transport(cows, limit)
compare_cow_transport_algorithms()





