import matplotlib.pyplot as plt
import pandas as pd
import re
import math
from decimal import *
import numpy
from sklearn import preprocessing

def data_preprocess(path):
	file = open(path)
	index = 0

	# get the data into two dimensions matrix
	result = []
	for row in file:
	   	if index > 1 and index < 38:
			result.append(row.split('\t')[1:-1])
		index = index + 1

	pattern = r'(\d*.\d*)%'

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
	return ans

def data_normalization(data):	
	Violent = data[3]
	Property = data[8]
	# Nonindex = data[14]

	y_v = []
	y_p = []
	# y_n = []
	for idx in range(0,len(data[0])):
		item = Violent[idx]
		y_v.append(item)
		item = Property[idx]
		y_p.append(item)
		# item = Nonindex[idx]
		# y_n.append(item)

	return y_v,y_p

def figure_generate(x,Violent_j,Property_j,Violent_a,Property_a):
	plt.subplot(2,1,1)
	plt.grid('on')
	plt.title('Violent Crime counts VS Property Crime counts')
	plt.plot(x,Violent_j,'r--',label = 'Juvenile Violent')
	plt.plot(x,Violent_a,'b--',label = 'Adult Violent')
	plt.xlabel('Year')
	plt.ylabel('Counts')
	plt.legend(loc='upper middle')
	plt.subplot(2,1,2)
	plt.grid('on')
	plt.plot(x,Property_j,'r--',label = 'Juvenile Property')
	plt.plot(x,Property_a,'b--',label = 'Adult Property')
	plt.xlabel('Year')
	plt.ylabel('Counts')
	# plt.gca().axes.get_yaxis().set_visible(False)
	plt.legend(loc='upper middle')
	plt.show()

path_a = 'ucr_export_adult.asp'
data_a =  data_preprocess(path_a)
Violent_a,Property_a = data_normalization(data_a)
path_j = 'ucr_export_juvenile.asp'
data_j = data_preprocess(path_j)
Violent_j,Property_j = data_normalization(data_j)
figure_generate(data_a[0],Violent_j,Property_j,Violent_a,Property_a)