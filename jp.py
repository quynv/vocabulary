#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import sys  
if sys.version_info >= (3,4):
    import importlib
    importlib.reload(sys)
elif sys.version_info <= (3.3) && sys.version_info >= (3.0):
    import imp
    imp.reload(sys)
else:
    reload(sys)
    sys.setdefaultencoding('utf-8')

def get_vocabulary():
    data = None
    vocabulary = ''
    with open('data.json') as data_file:
        data = json.load(data_file)
    if not data:
        return "Error"
    word = random.choice(data);
    vocabulary = word['Japanese'] + "("+ word['Kana'] +"): " + word['Vietnamese']
    return vocabulary
