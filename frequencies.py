"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
#Please commit

def frequencies(items):
    frequencies = {}
    # Your code goes here
    
    for x in range(len(items)):
        if str(items[x]) in list(frequencies):
            frequencies[str(items[x])] = frequencies[str(items[x])] + 1
        else:
            frequencies[str(items[x])] = 1
    
    return frequencies



