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
	return ans

def data_normalization(adult_,juvenile,population):	
	y_adult = adult_[2]
	x_adult = adult_[0]
	x = x_adult
	y_juvenile = juvenile[2]
	x_juvenile = juvenile[0]	

	y = []
	y_j = []
	y_a = []
	for idx in range(0,len(population)):
		item = math.log(population[idx])
		y.append(item)
		item = math.log(y_juvenile[idx]) + 3.1
		y_j.append(item)
		item = math.log(y_adult[idx])
		y_a.append(item)

	# population_normalized = preprocessing.normalize(y, norm='l1')[0]
	# juvenile_normalized = preprocessing.normalize(y_j, norm='l1')[0]
	# adult_normalized = preprocessing.normalize(y_a, norm='l1')[0]
	# return adult_normalized,juvenile_normalized,population_normalized
	return y_a,y_j,y

def figure_generate(x,population_normalized,juvenile_normalized,adult_normalized):
	plt.title('Juvernile Population Trend VS. Arrested Juvenile Trend')
	plt.xlabel('Year')
	plt.ylabel('Trend')
	plt.grid('on')
	plt.plot(x,population_normalized,'ro',label = 'Juvenile Population Trend')
	plt.plot(x,juvenile_normalized,'bo',label = 'Arrested Juvenile Trend')
	plt.gca().axes.get_yaxis().set_visible(False)
	plt.legend(loc='lower left')
	plt.show()

all_path = 'ucr_export.asp'
all_age = data_preprocess(all_path)
adult_path = 'ucr_export_adult.asp'
adult_ = data_preprocess(adult_path)
juvenile_path = 'ucr_export_juvenile.asp'
juvenile = data_preprocess(juvenile_path)
population = [68640942,69473151,70233520,70920754,71431424,71946064,72376189,72671175,72936457,73100758,73297735,73523669,73757714,74019405,74104602,74134167,74123035,73917090,73710072]
a_norm,j_norm,p_norm = data_normalization(adult_,juvenile,population)
figure_generate(adult_[0],p_norm,j_norm,a_norm)
