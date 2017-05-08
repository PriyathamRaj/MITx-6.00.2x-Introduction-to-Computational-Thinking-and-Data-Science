# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:04:04 2017

@author: Priyatham
"""
import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    same = 0
    
    for i in range(numTrials):
        bucket = ['r','g'] * 4
        three = []
        for i in range(3):
            chosen = random.choice(bucket)
            bucket.remove(chosen)
            three.append(chosen)
        if three[0] == three[1] == three[2]:
            same += 1
    
    return (same/numTrials)