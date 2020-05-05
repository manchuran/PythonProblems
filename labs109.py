# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:50:15 2020

@author: sauer
"""

def is_ascending(items):
    if len(items) <= 1:
        return True
    
    chunk = len(items) // 2
    
    one_half = items[:chunk]
    second_half = items[chunk:]

    
    if (second_half[0] <= one_half[-1]):
        return False

    if len(one_half) >= 2:
        if is_ascending(one_half) is False:
            return False
        
    if len(second_half) >= 2:
        if is_ascending(second_half) is False:
            return False

    return True



def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust