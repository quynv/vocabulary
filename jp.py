#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import sys  
import platform
current_version = platform.python_version()
if current_version >= '3.4':
    import importlib
    importlib.reload(sys)
elif current_version <= '3.3':
    import imp
    imp.reload(sys)
else:
    reload(sys)

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
