# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:14:30 2022

@author: litvinov
"""
a = [input(), input(), input(), input()]
#a = ['Hello', '2', 'world', ':-)']

def Dlinna(List):
    for i in List:
        len1 = len(i)
        if len1 <= 3:
            print(i)

Dlinna(a)
                
