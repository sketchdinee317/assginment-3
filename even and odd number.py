# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:30:45 2022

@author: admin
"""

sum_even=0
sum_odd=0
for i in range(4,6):
    if i%2==0:
        sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i
print("sum of even number",sum_even)
print("sum of odd number",sum_odd)