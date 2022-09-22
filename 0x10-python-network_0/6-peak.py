#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak"""
    if list_of_integers:
        peak = list_of_integers[0]
        for i in list_of_integers:
            if i > peak:
                peak = i
        return peak
    else:
        return None
