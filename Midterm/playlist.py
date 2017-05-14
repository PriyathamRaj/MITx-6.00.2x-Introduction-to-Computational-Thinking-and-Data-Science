# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:25:24 2017

@author: Priyatham
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    
    sizes = [i[2] for i in songs]
    d = dict()
    for item in songs:
        d[item[2]] = item[0]
    
    total_size = 0
    play_list = []
    size_list = []
            
    if sizes[0] > max_size:
        return []
    else:
        size_list.append(sizes[0])
        total_size += sizes[0]
        
    sizes_inc = sorted(sizes[1:])
    
    for size in sizes_inc:
        if total_size + size <= max_size:
            size_list.append(size)
            total_size += size
        
    for item in size_list:
        play_list.append(d[item])
        
    return play_list

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),
         ('Wannabe',2.7, 1.2)]

print(song_playlist(songs, 12.2))
        
        
