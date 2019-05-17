# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:38:52 2019

@author: abhin
"""
import random 
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
final = list(map(lambda x : random.choice(code_names), names))

print(final)