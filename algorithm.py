import random
from math import inf

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

# 1
# The task of finding the easiest way for graph with some weight
class Graph():
	def __init__(self, lengh, weight): # lengh — lengh of graph without start and end; weight — mas of weight, which will take by randint for weight of ribs
		self.lengh=lengh
		self.weight=weight
		self.res_way=[]
		self.res_weight=0
		self.node=[]
		self.connect={}
		self.weight_node_by_their_place={}

	def __str__(self):
		return 'Class for count the easiest way of graph with some weight!'

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

	def find_the_weight(self):
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
		self.weight_node_by_their_place=time_weight
		return self.res_weight

	def find_the_way(self):
		time_way={}
		time_way[f'{self.node[0]}']='—'
		for c in range(len(self.node[1])):
			time_way[f'{self.node[1][c]}']=f'{self.node[0]} > {self.node[1][c]}'
		for c in range(2,len(self.node)):
			if type(self.node[c])==str:
				for ccc in self.connect:
					cccc=ccc.split('==>')
					if cccc[1]==self.node[c]:
						if self.connect[ccc]+self.weight_node_by_their_place[cccc[0]]==self.res_weight:
							time_way[f'{cccc[1]}']=f"{time_way[f'{cccc[0]}']} > {cccc[1]}"
			else:
				for cc in range(len(self.node[c])):
					for ccc in self.connect:
						cccc=ccc.split('==>')
						if cccc[1]==self.node[c][cc]:
							if self.connect[ccc]+self.weight_node_by_their_place[f'{cccc[0]}']==self.weight_node_by_their_place[f'{cccc[1]}']:
								time_way[f'{cccc[1]}']=f"{time_way[f'{cccc[0]}']} > {cccc[1]}"
		self.res_way=time_way[f'{self.node[len(self.node)-1]}']
		return self.res_way

def done_graph(lengh, weight):
	g=Graph(lengh=lengh, weight=weight)
	print('Node: ', end='')
	print(g.create_a_node_for_graph())
	print('Connection: ', end='')
	print(g.create_a_connections_for_graph())
	print('Result weight: ', end='')
	print(g.find_the_weight())
	print('Result way: ', end='')
	print(g.find_the_way())

# done_graph(5, [1,2,3,4,5])

# More rightly algorithm for searching the easiest way of graph with some weight
class GraphRight():
	def __init__(self, lengh, weight):
		self.lengh=lengh
		self.weight=weight
		self.res_way=[]
		self.res_weight=0
		self.node=[]
		self.connect={}

	def __str__(self):
		return 'Class for count the easiest way of graph with some weight!'

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

	def find_the_graph(self):
		time_variable_for_weight={}
		time_variable_for_way={}
		for c in range(len(self.node)):
			if type(self.node[c])==str:
				time_variable_for_weight[self.node[c]]=inf
			else:
				for cc in range(len(self.node[c])):
					time_variable_for_weight[self.node[c][cc]]=inf
		time_variable_for_weight[self.node[0]]=0
		time_variable_for_way[self.node[0]]=None
		for c in range(len(self.node[1])):
			time_variable_for_weight[self.node[1][c]]=self.connect[f'{self.node[0]}==>{self.node[1][c]}']
			for cc in self.connect:
				ccc=cc.split('==>')
				if ccc[1]==self.node[1][c]:
					time_variable_for_way[self.node[1][c]]=f'{ccc[0]} > {ccc[1]}'
		for c in range(2, len(self.node)):
			if type(self.node[c])==str:
				for ccc in self.connect:
					cccc=ccc.split('==>')
					if cccc[1]==self.node[c]:
						if time_variable_for_weight[self.node[c]]>self.connect[ccc]+time_variable_for_weight[cccc[0]]:
							time_variable_for_weight[self.node[c]]=self.connect[ccc]+time_variable_for_weight[cccc[0]]
							time_variable_for_way[self.node[c]]=f'{time_variable_for_way[cccc[0]]} > {cccc[1]}'
			else:
				for cc in range(len(self.node[c])):
					for ccc in self.connect:
						cccc=ccc.split('==>')
						if cccc[1]==self.node[c][cc]:
							if time_variable_for_weight[self.node[c][cc]]>self.connect[ccc]+time_variable_for_weight[cccc[0]]:
								time_variable_for_weight[self.node[c][cc]]=self.connect[ccc]+time_variable_for_weight[cccc[0]]
								time_variable_for_way[self.node[c][cc]]=f'{time_variable_for_way[cccc[0]]} > {cccc[1]}'
		self.res_way=time_variable_for_way[self.node[len(self.node)-1]]
		self.res_weight=time_variable_for_weight[self.node[len(self.node)-1]]
		return self.res_weight, self.res_way

def done_right_graph(lengh, weight):
	g=GraphRight(lengh=lengh, weight=weight)
	print('Node: ', end='')
	print(g.create_a_node_for_graph())
	print('Connection: ', end='')
	print(g.create_a_connections_for_graph())
	gg=g.find_the_graph()
	print('Result weight: ', end='')
	print(gg[0])
	print('Result way: ', end='')
	print(gg[1])

# done_right_graph(3, [1,2,3,4])

# The task of finding the shortest way for graph without some weight
class GraphWithoutWeight():
	def __init__(self, lengh):
		self.lengh=lengh
		self.node=[]
		self.connect=[]
		self.step=None
		self.res_way=None

	def __str__(self):
		return f'This algorithm of counting the shortest way from start to finish'

	def create_a_node(self):
		node_2=[]
		self.node.append('(1,start)')
		for x in range(self.lengh):
			for y in range(random.randint(1,3)): # level
				node_2.append(f'({x + 2}.{y+1})')
			self.node.append(node_2)
			node_2=[]
		self.node.append(f'({self.lengh + 2},finish)')
		return self.node

	def create_a_connect(self):
		for c in range(len(self.node[1])):
			self.connect.append(f'{self.node[0]}==>{self.node[1][c]}')
		for cc in range(1, self.lengh):
			for c in range(len(self.node[cc])):
				for n in range(len(self.node[cc+1])):
					self.connect.append(f'{self.node[cc][c]}==>{self.node[cc+1][n]}')
		for c in range(len(self.node[self.lengh])):
			self.connect.append(f'{self.node[self.lengh][c]}==>{self.node[self.lengh+1]}')
		for c in range(len(self.node)-4): # non-standart connect
			if type(self.node[c])==str: # first element in array
				num1 = random.randint(0,1)
				if num1 == 1:
					check=0
					num2 = random.randint(2,3)
					for cc in range(len(self.node[c+num2])):
						num3 = random.randint(0,1)
						if num3==1:
							self.connect.append(f'{self.node[c]}==>{self.node[c+num2][cc]}')
							check+=1
					if check==0:
						self.connect.append(f'{self.node[c]}==>{self.node[c+num2][0]}')
			else:
				for cc in range(len(self.node[c])):
					num1 = random.randint(0,1)
					if num1==1:
						check=0
						num2=random.randint(2,3)
						if type(self.node[c+num2])==str:
							self.connect.append(f'{self.node[c][cc]}==>{self.node[c+num2]}')
						else:
							for ccc in range(len(self.node[c+num2])):
								num3=random.randint(0,1)
								if num3==1:
									self.connect.append(f'{self.node[c][cc]}==>{self.node[c+num2][ccc]}')
									check+=1
							if check==0:
								self.connect.append(f'{self.node[c][cc]}==>{self.node[c+num2][0]}')
		for c in range(len(self.node[len(self.node)-3])): # non-standart connect too
			num1=random.randint(0,1)
			if num1==1:
				self.connect.append(f'{self.node[len(self.node)-3][c]}==>{self.node[len(self.node)-1]}')
		return self.connect

	def find_way(self):
		time_step={}
		time_way={'(1,start)':'(1,start)'}
		for c in range(len(self.node)):
			if type(self.node[c])==str:
				time_step[self.node[c]]=inf
			else:
				for cc in range(len(self.node[c])):
					time_step[self.node[c][cc]]=inf
		time_step['(1,start)']=0
		for c in range(len(self.node[1])):
			time_step[self.node[1][c]]=1
			time_way[self.node[1][c]]=f'{self.node[0]} > {self.node[1][c]}'
		for c in range(2,len(self.node)):
			if type(self.node[c])==str:
				for cc in self.connect:
					ccc=cc.split('==>')
					if ccc[1]==self.node[c]:
						if time_step[ccc[1]]>time_step[ccc[0]]+1:
							time_step[ccc[1]]=time_step[ccc[0]]+1
							time_way[ccc[1]]=f'{time_way[ccc[0]]} > {ccc[1]}'
			else:
				for cc in range(len(self.node[c])):
					for ccc in self.connect:
						cccc=ccc.split('==>')
						if cccc[1]==self.node[c][cc]:
							if time_step[cccc[1]]>time_step[cccc[0]]+1:
								time_step[cccc[1]]=time_step[cccc[0]]+1
								time_way[cccc[1]]=f'{time_way[cccc[0]]} > {cccc[1]}'
		self.step=time_step[self.node[len(self.node)-1]]
		self.res_way=time_way[self.node[len(self.node)-1]]
		return self.step, self.res_way

def done_graph_without_weight(lengh):
	g=GraphWithoutWeight(lengh=lengh)
	print('Node: ', end='')
	print(g.create_a_node())
	print('Connect:', end='')
	print(g.create_a_connect())
	gg=g.find_way()
	print('Result way: ', end='')
	print(gg[1])
	print('Total step: ', end='')
	print(gg[0])

# done_graph_without_weight(3)

# 2
# Greedy algorithm
class Greedy():
	def __init__(self, allow_tower, num_of_needed_states):
		self.num_of_needed_states=num_of_needed_states
		self.must_cover=[]
		self.allow_states=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
		self.cover_tower={}
		self.price_tower={}
		self.allow_tower=['KVLY-TV mast','KXJB-TV mast','KXTV/KOVR tower','Petronius Platform','KCAU TV Tower','KATV Tower','WECT TV6 Tower','WOI-Tower','AFLAC Tower','WBTV-Tower','WTTO Tower','WCSC-Tower','KTVE-Tower','WCTV Tower','TV Alabama Tower','KDLT Tower','KY3 Tower','KLDE Tower','WLBT Tower','WCIX TV Tower','KYTV Tower 2','Hoyt Radio Tower','WNCN Tower','KHYS Tower','WNCN Tower 2','KELO TV Tower','KHOU-TV Tower','KTRK-TV Tower','Fox-TV Tower','WCNC-TV Tower','WFMY Tower','WTVY-TV Tower','KLKN Tower','KBIM Tower']
		self.must_tower_to_use=[]
	
	def __str__(self):
		return f'This algorithm find a town, which you must to use for cover your states'
	
	def fill_must_cover(self):
		for c in range(self.num_of_needed_states):
			cc=random.choice(self.allow_states)
			if cc in self.must_cover:
				while cc in self.must_cover:
					cc=random.choice(self.allow_states)
				self.must_cover.append(cc)
			else:
				self.must_cover.append(cc)
		return self.must_cover

	def fill_cover_tower(self):
		for c in self.allow_tower:
			self.cover_tower[c]=random.choice(self.allow_states)
		for c in range(4):
			for cc in range(4):
				ccc=random.choice(self.allow_states)
				cccc=self.cover_tower[self.allow_tower[c]].split(',')
				if ccc in cccc:
					while ccc in cccc:
						ccc=random.choice(self.allow_states)
					self.cover_tower[self.allow_tower[c]]=f'{self.cover_tower[self.allow_tower[c]]},{ccc}'
				else:
					self.cover_tower[self.allow_tower[c]]=f'{self.cover_tower[self.allow_tower[c]]},{ccc}'
		for c in range(4, 24):
			for cc in range(1):
				ccc=random.choice(self.allow_states)
				cccc=self.cover_tower[self.allow_tower[c]].split(',')
				if ccc in cccc:
					while ccc in cccc:
						ccc=random.choice(self.allow_states)
					self.cover_tower[self.allow_tower[c]]=f'{self.cover_tower[self.allow_tower[c]]},{ccc}'
				else:
					self.cover_tower[self.allow_tower[c]]=f'{self.cover_tower[self.allow_tower[c]]},{ccc}'
		return self.cover_tower
		
	def fill_price_tower(self):
		for c in range(len(self.allow_tower)):
			if len(self.cover_tower[self.allow_tower[c]].split(','))==5:
				self.price_tower[self.allow_tower[c]]=random.randint(4000, 5000)
			elif len(self.cover_tower[self.allow_tower[c]].split(','))==2:
				self.price_tower[self.allow_tower[c]]=random.randint(1000, 2000)
			else:
				self.price_tower[self.allow_tower[c]]=random.randint(500, 1000)
		return self.price_tower

	def find_tower(self):
		var_for_used_tower=[]
		var_for_price=[]
		var1=set(self.must_cover)
		for c in self.allow_tower:
			var2=set(self.cover_tower[c].split(','))
			if var2.intersection(var1)==var2:
				var_for_used_states=var2
				var_for_used_tower.append(c)
				var_for_price.append(self.price_tower[c])
				for cc in var_for_used_states:
					self.must_cover.remove(cc)
			var1=set(self.must_cover)
		self.must_tower_to_use=var_for_used_tower
		price=sum(var_for_price)
		return self.must_tower_to_use, price
	
def done_greedy(num_of_needed_states, allow_tower):
	g=Greedy(num_of_needed_states=num_of_needed_states, allow_tower=allow_tower)
	print('\nState that must be covering: ', end='')
	print(g.fill_must_cover())
	print('\nInfo about radio tower: ', end='')
	print(g.fill_cover_tower())
	print(g.fill_price_tower())
	gg=g.find_tower()
	print('\nFor cover your states, you must to use this radio tower: ', end='')
	print(gg[0])
	print('\nFinal price: ', end='')
	print(gg[1])
	
done_greedy(num_of_needed_states=7, allow_tower=0) # num_of_needed_states must be less then 50 (50 is max)

# One more greedy algorithm, but for max (thief)

# 3
# The task of traveling Camewoyzer
