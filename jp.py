#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import sys  
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