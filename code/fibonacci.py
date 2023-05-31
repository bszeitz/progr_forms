# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:39:21 2023

@author: User
"""


def fibonacci(n):
    
    F0 = 0
    F1 = 1
    
    if n == 0 :
        Fn = 0
    elif n == 1 :
        Fn = 1
    else :
        #Fn = 0
        Fn_1 = 1 
        Fn_2 = 0
        for i in range(n-1) :
            Fn = Fn_1 + Fn_2
            Fn_2 = Fn_1
            Fn_1 = Fn
    
    
    # function body 

    return Fn