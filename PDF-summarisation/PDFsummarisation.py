#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 01:15:22 2019

@author: abhijithneilabraham
"""

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from pattern.web import URL, PDF
pdf2=PDF('forests-10-00219-v2.pdf')
text2=pdf2.string
print(summarize(text2))
print('---------------------------------------------------')
'''
for increasing or decreasing the summarisation ratio, give a value for the ratio parameter
'''
print(summarize(text2, ratio=0.009))

print(keywords(text2))
print('----------------------------------------------------')
'''
the word_count paramter limits the max number of words used in the summary
'''
print(summarize(text2,word_count=100))
