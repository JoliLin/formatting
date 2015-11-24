import numpy as np
import sys
from collections import defaultdict, deque
from concurrent.futures import ProcessPoolExecutor
from io import open
from itertools import izip

def zeroSampling( f_ ):
	g = from_adjlist(f_)

	c = g.convert2matrix()
	r = g.relation()

	f = np.dot( r, c )

	return f 

def get_zero(  file_ ):
	user = deque()
	item = deque()
	value = deque()
	
	count = 0
	for nd in file_:
		relation = nd.tolist()
		count2 = 0
		for element in relation:
			if element == 0:
				user.append(count)
				item.append(count2)
				value.append(0)
			count2 = count2 + 1
		count = count + 1
	
	return user, item, value

def from_adjlist( adjlist ):
	g = Graph()

	for item in adjlist:
		s = item.split(' ')
		g[int(s[0])] = map(int, s[1:])
	
	return g

class Graph(defaultdict):
	def __init__(self):
		super(Graph, self).__init__(list)

	def get_users(self):
		return self.keys()

	def get_items(self):
		return set([item for key in self.keys() for item in self.get(key)])

	def adj_iter(self):
		return self.iteritems()

	def relation(self):
		numOfusers = len(self.get_users())
		self.relation = np.zeros(shape=( numOfusers, numOfusers ))

		for item in self.keys():
			for item2 in self.keys():
				if item is not item2:
					if len(set(self.get(item)) & set(self.get(item2))) > 0:
						self.relation[item][item2] = 1

		return self.relation

	def convert2matrix(self):
		numOfusers = len(self.get_users())
		numOfitems = len(self.get_items())
		self.matrix = np.zeros(shape=( numOfusers, numOfitems ))
	
		for user in self.keys():
			for item in self.get(user):
				self.matrix[user][item] = 1

		return self.matrix
		
