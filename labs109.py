# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:50:15 2020

@author: sauer
"""

def counting_series(n):
    '''
    Question:
    The counting series "1234567891011121314151617181920212223"... is an 
    infinitely long string of digits 0-9 that consists of the positive integers 
    written in ascending order without any separators between the individual 
    numbers. This function should return the integer digit that is in the position n 
    of the counting series, with positions starting from 0 as usual in computing
    
    Solution:
    Obtain closed form solution of the index of the largest n-digit number
    and iterate backwards from that to digit in question
    '''
    #For numbers less than 9, simply return n+1
    if n < 9:
        return n+1
    
    #Initialize values of m and s
    m, s = 1, 0
    
    #Obtain index of largest digit; index is lower than n
    while (s<=n):
        s = (9*(10**m *(m+1)) - 10**(m+1) + 1)//9
        m+=1
    #Obtain largest digit in interval
    upper_limit = int(str(9)*(m-1))
    
    #Iterate through largest digit to establish
    #how far backwards to go in calculating distance from
    #largest digit to n
    k=0
    d=((s-1)-n)
    while d%(m-1) != 0:
        d-=1
        k+=1
    number = upper_limit - d//(m-1)
    
    #return string at location -1-k
    return str(number)[-1-k]



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