# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:51:37 2017

@author: Priyatham
"""

import numpy as np
import random

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.

    Hint: You might want to use bin() on an int to get a string, get rid of the first two characters,
    add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.
    
    If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
    If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
    If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
    """
    results = powerset(choices)
    sum_dict = dict()
    for item in results:
        product = sum(choices * item)
        if product <= total:
            if product in sum_dict.keys():
                sum_dict[product].append(item)
            else:
                sum_dict[product] = [item]
    
    if total not in sum_dict.keys():
        total = max([i for i in sum_dict.keys() if i<total])
        
    sum_list = [sum(item) for item in sum_dict[total]]
    return random.choice([item for item in sum_dict[total] if sum(item) == min(sum_list)])
    
    
def powerset(L):
    combo_set = []
    n = len(L)
    for i in range(2**n):
        combo = []
        for j in range(n):
            if (i>>j) % 2 == 1:
                combo.append(1)
            else:
                combo.append(0)
        combo_set.append(np.array(combo))
    return combo_set
    
def bin_set(L):
	combos = []
	for item in L:
		binary = bin(item)
		arr = binary[2:]
		if len(arr) < len(L):
			arr = [0]*(len(L) - len(arr)) + arr
		combos.append(np.array(arr))
	return combos
    
    
    
    
    
