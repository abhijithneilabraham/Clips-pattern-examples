#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:30:27 2019

@author: abhijithneilabraham
"""

from nltk.stem import WordNetLemmatizer
'''
According to the issue #254
the singularise function needs to be updated.
So,trying to use the wordnetlemmatizer here for 
redefining the function and getting better results
'''

def singularize(keyw):
    wnl = WordNetLemmatizer()
    singular=wnl.lemmatize(keyw)
    return singular
print(singularize("pennies"))
  