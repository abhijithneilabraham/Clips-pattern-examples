#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:13:52 2019

@author: abhijithneilabraham
"""

from translate import Translator
lang="German"
keyw="How are you?"
def translated(lang,keyw):
    translator= Translator(to_lang=lang)
    translation = translator.translate(keyw)
    return translation
print(translated("German","find me the cook"))