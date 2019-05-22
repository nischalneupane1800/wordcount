from django.http import HttpResponse
from django.shortcuts import render
import operator



def homepage(request):
	return render(request,'home.html')

def count(request):
	data = request.GET['fulltextarea']
	split = data.split()
	count = len(split)

	dict = {}

	for word in split:
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1

	sorted_list = sorted(dict.items(), key = operator.itemgetter(1))
	
	return render(request,'count.html',{ 'fulltextarea' : data, 'split' : count, 'dict' : sorted_list})