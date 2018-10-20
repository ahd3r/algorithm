from time import sleep
import random
# from math import inf

# Try to use a call def by other def
def tryy():
	print('HI')

def try_try():
	tryy()

# try_try()

# Try sleep function
def print_item_of_mas(mas):
	for item in mas:
		sleep(1)
		print(item)

# print_item_of_mas([1,2,3,4,5,6,7,8,9])

# Algorithm quick sort
def qs(mas):
	if len(mas)<=1:
		return mas
	else:
		pivot=mas[0]
		less_then_pivot=[i for i in mas[1:] if i <= pivot]
		more_then_pivot=[i for i in mas[1:] if i > pivot]
		return qs(less_then_pivot)+[pivot]+qs(more_then_pivot)

# print(qs([36,256,32,76,36,4326,543,4,85,3,1,534,7,653,473]))

#---------------------------------------------------------------------

# 1
# The task of finding the easiest way for graph with some weight
class Graph():
	def __init__(self, lengh, weight): # lengh — lengh of graph without start and end; weight — mas of weight, which will take by randint for weight of ribs
		self.lengh=lengh
		self.weight=weight
		self.res_way=[]
		self.res_weight=None
		self.node=[]
		self.connect={}

	def __str__(self):
		return 'Class for count the easiest way for graph with some weight!'

	def create_a_node_for_graph(self):
		node_2=[]
		self.node.append('(1,start)')
		for x in range(self.lengh):
			for y in range(random.randint(1,3)): # level
				node_2.append(f'({x + 2}.{y+1})')
			self.node.append(node_2)
			node_2=[]
		self.node.append(f'({self.lengh + 2},finish)')
		return self.node

	def create_a_connections_for_graph(self):
		for c in range(len(self.node[1])):
			self.connect[f'{self.node[0]}==>{self.node[1][c]}']=random.choice(self.weight)
		for cc in range(1, self.lengh):
			for c in range(len(self.node[cc])):
				for n in range(len(self.node[cc+1])):
					self.connect[f'{self.node[cc][c]}==>{self.node[cc+1][n]}']=random.choice(self.weight)
		for c in range(len(self.node[self.lengh])):
			self.connect[f'{self.node[self.lengh][c]}==>{self.node[self.lengh+1]}']=random.choice(self.weight)
		return self.connect

	def find_the_way(self):
		time_weight={'(1,start)': 0}
		res_for_graph=[]
		some=[]
		for r in self.connect.values():
			res_for_graph.append(r)
		for c in range(len(self.node[1])):
			time_weight[f'{self.node[1][c]}']=res_for_graph[c]
		for c in range(2, len(self.node)):
			if type(self.node[c])==list:
				for cc in range(len(self.node[c])):
					for ccc in self.connect:
						cccc=ccc.split('==>')
						if cccc[1]==self.node[c][cc]:
							for ccccc in self.node[c-1]:
								some.append(self.connect[f'{ccccc}==>{cccc[1]}']+time_weight[f'{ccccc}'])
							some.sort()
							time_weight[f'{self.node[c][cc]}']=some[0]
							some=[]
			else:
				for cc in range(len(self.node[c-1])):
					some.append(self.connect[f'{self.node[c-1][cc]}==>{self.node[c]}']+time_weight[f'{self.node[c-1][cc]}'])
				some.sort()
				time_weight[f'{self.node[c]}']=some[0]
				some=[]
		self.res_weight=time_weight[f'({self.lengh+2},finish)']
		return self.res_way, self.res_weight, time_weight

def done_graph(lengh, weight):
	g=Graph(lengh=lengh, weight=weight)
	print(g.create_a_node_for_graph())
	print(g.create_a_connections_for_graph())
	gg=g.find_the_way()
	print(f'Result way: {gg[0]}')
	print(f'Result weight: {gg[1]}')
	print(f'Time weight: {gg[2]}')

done_graph(3, [1,2,3,4])

# The task of finding the easiest way for graph with some weight include negative

# The task of finding the shortest way for graph without some weight

# The graph without directions

# 2
# The task of covering states

# 3
# The task of traveling Camewoyzer
