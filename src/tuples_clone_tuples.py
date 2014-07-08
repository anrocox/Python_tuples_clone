#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

How to clone a tuple in python?

¿Como clonar una tupla en python?
'''

from copy import deepcopy

#create a tuple
tupla = ('hello', 2, [], True)
print (tupla)

#make a copy of a tuple using deepcopy() function
tupla_clone = deepcopy(tupla)

#Make changes the tupla_clone
tupla_clone[2].append(100)
print(tupla_clone)
print(tupla)
