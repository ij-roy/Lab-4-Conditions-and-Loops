# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:09:05 2023

@author: LAB
"""

n = int(input("enter a number n : "))
i = 1
f = 1
while i<=n:
    f = f*i
    i = i+1
print("factorial of the number is",f)