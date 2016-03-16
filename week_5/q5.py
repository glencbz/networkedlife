p = 0.3
edgelist = [[1, 2, 6], [0, 3, 7], [0, 3, 4, 5], [1, 2, 4, 5], [2, 3, 5, 6], [2, 3, 4, 7], [0, 4, 7], [1, 5, 6]]

class Node:

	def __init__(self, network, n, infected=False):
		self.id = n
		self.infected = infected
		self.network = network

	def __str__(self):
		return str(self.id + 1) + (" NOT" if not self.infected else "") + " INFECTED"

	def update(self):
		if self.infected:
			return False
		neighbours = [self.network.nodes[i] for i in edgelist[self.id]]
		total = len(neighbours)
		infected = 0
		for neighbour in neighbours:
			if neighbour.infected:
				infected+=1
		if float(infected)/ total > p:
			return True
		return False

	def infect(self):
		self.infected = True

class Network:

	def __init__(self):
		self.nodes = [Node(self,i) for i in range(8)]

	def update(self):
		stop = False
		while not stop:
			stop = True
			update_list = [node.update() for node in self.nodes]
			for i in range(len(update_list)):
				if update_list[i]:
					self.nodes[i].infect()
					stop = False
		for i in self.nodes:
			print i

def part1():
	print 'PART 1\n\n'
	n = Network()
	n.nodes[0].infect()
	n.update()

def part2():
	print 'PART 2\n\n'
	n = Network()
	n.nodes[2].infect()
	n.update()

part1()
part2()