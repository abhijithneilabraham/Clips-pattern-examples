#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:13:52 2019

@author: abhijithneilabraham
"""


def translated(lang,keyw):
    translator= Translator(to_lang=lang)
    translation = translator.translate(keyw)
    return translation
from translate import Translator
from pattern.web import Twitter, plaintext
twitter = Twitter(language='en') 
for tweet in twitter.search('"more important than"', cached=False):
    #print(plaintext(tweet.text))
    print(translated('German',plaintext(tweet.text)))