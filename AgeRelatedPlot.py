import matplotlib.pyplot as plt
import pandas as pd
import re
import math
from decimal import *

def data_preprocess(path):
	file = open(path)
	index = 0

	# get the data into two dimensions matrix
	result = []
	for row in file:
	   	if index > 1 and index < 38:
			result.append(row.split('\t')[1:-1])
		index = index + 1

	pattern = r'(\d+)%'

	ans = []
	for item in result:
		sub = []
		for word in item:
			word = word.replace(',','')
			word = word.replace('**','0')
			num = re.findall(pattern, word)
			if num:
				#avoid rounding to zero
				word = (float(num[0])/100.0)
			else:
				word = int(word)
			sub.append(word)
		ans.append(sub)
	print ans

path = 'ucr_export.asp'
print data_preprocess(path)