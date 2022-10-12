"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
#Please commit

def frequencies(items):
    frequencies = {}
    # Your code goes here
    
    for x in range(len(items)):
        if items[x] in list(frequencies):
            frequencies[items[x]] = frequencies[items[x]] + 1
        else:
            frequencies[items[x]] = 1
    
    return frequencies
