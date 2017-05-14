# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:28:00 2017

@author: Priyatham
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    max_so_far = 0
    sub_sum = 0
    
    for i in range(len(L)):
        sub_sum += L[i]
        if sub_sum > max_so_far:
            max_so_far = sub_sum
        elif sub_sum < 0:
            sub_sum = 0
            
    return max_so_far

L = [-2,-3,4,-1,-2,1,5,-3]

print(max_contig_sum(L))
            
