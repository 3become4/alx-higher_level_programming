#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.copy()
    k = list(x.keys())
    for i in k:
        x[i] *= 2
    return (x)
