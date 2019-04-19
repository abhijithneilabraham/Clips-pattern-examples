#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:42:05 2019

@author: abhijithneilabraham
"""

import json
from pprint import pprint

data = json.load(open('jsons/download.jpeg.json'))
pprint(data["textAnnotations"][0]['description'])
