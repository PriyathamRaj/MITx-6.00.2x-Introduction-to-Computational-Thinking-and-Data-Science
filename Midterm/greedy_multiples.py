# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:31:46 2017

@author: Priyatham
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    if L == []:
        return 'no solution'
        
        
    
    # sum of the product of multiples and list elements
    m_sum = 0
    # initialize list of multiples
    m = list()
    s_copy = s
    
    for item in L:
        mult = 0
        s_copy -= m_sum
        m_sum = 0
        
        while m_sum <= s_copy:
            mult += 1
            m_sum = item * mult
        
        if mult != 0:
            mult -= 1
            m_sum = item * mult
        
        m.append(mult)

    check = 0
    for i in range(len(L)):
        check += L[i] * m[i]
    
    if check == s:
        return sum(m)
    else:
        return 'no solution'
            
L = [10,5,1]
s = 14
print(greedySum(L,s))