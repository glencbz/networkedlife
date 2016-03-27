#Networked Life HW 4

#####Glen Choo 1000472
#####Loo Juin 1000546
#####Tan Hao Qin 1000521

##Exercise 1

####Part a

$$
\begin{bmatrix}
0&0&1&1&0&0&0&0\\
0&0&0&0&1&1&0&0\\
0&0&0&0&0&0&1&0\\
0&0&0&0&0&0&1&0\\
0&0&0&0&0&0&1&1\\
0&0&0&0&0&0&0&1\\
0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0
\end{bmatrix} 
$$

####Part b

$$
\begin{bmatrix}
&0&0&0&0&0&0&0&0\\
&0&0&0&0&0&0&0&0\\
&0&0&1&1&0&0&0&0\\
&0&0&1&1&0&0&0&0\\
&0&0&0&0&1&1&0&0\\
&0&0&0&0&1&1&0&0\\
&0&0&0&0&0&0&3&2\\
&0&0&0&0&0&0&2&3
\end{bmatrix} 
$$

$C_{75}$ is still $0$, $C_{78}$ is now $1$, 
The number of articles that cite both i and j.

####Part c
$A^3$ is all zeroes. The entries in $A^m$ represent the number of paths from i to j with length = m. Therefore there are no feasible paths of length 3.

##Exercise 2

a)
####Degree Centrality
$$
\begin{array}{c|c}
\text{Node}&\text{Degree} \\
\hline
1&3 \\
2&2 \\
3&3 \\
4&3 \\
5&3
\end{array}
$$

####Closeness Centrality
$$\begin{align}
C_1 &= \frac{n-1}{d_{12}+d_{13}+d_{14}+d_{15}} \\
&= \frac{5-1}{1 + 1 + 1 + 2} \\
&= 0.80 \\
\\
C_2 &= \frac{n-1}{d_{21}+d_{23}+d_{24}+d_{25}} \\
&= \frac{5-1}{1 + 2 + 2 + 1} \\
&= 0.66 \\
\\
C_3 &= \frac{n-1}{d_{31}+d_{32}+d_{34}+d_{35}} \\
&= \frac{5-1}{1 + 2 + 1 + 1} \\
&= 0.80 \\
\\
C_4 &= \frac{n-1}{d_{41}+d_{42}+d_{43}+d_{45}} \\
&= \frac{5-1}{1 + 2 + 1 + 1} \\
&= 0.80 \\
\\
C_5 &= \frac{n-1}{d_{51}+d_{52}+d_{53}+d_{54}} \\
&= \frac{5-1}{2 + 1 + 1 + 1} \\
&= 0.80
\end{align}$$

In summary:
$$
\begin{array}{c|c}
\text{Node}&\text{Closeness} \\
\hline
1&0.80 \\
2&0.66 \\
3&0.80 \\
4&0.80 \\
5&0.80
\end{array}
$$

####Eigenvector Centrality

Let $A$ be the adjacency matrix of this graph.
$$\begin{align}
A &=
\begin{bmatrix}
0&1&1&1&0 \\
1&0&0&0&1 \\
1&0&0&1&1 \\
1&0&1&0&1 \\
0&1&1&1&0
\end{bmatrix}
\end{align}$$

Python was used for computation.

Python code:
```
import numpy as np


# Finds the index of the max element in the ndarray.
def find_max_index(a):
	top = a.shape[0]
	max_index = 0
	cur_max = None
	for i in range(top):
		if cur_max is None or a[i] > cur_max:
			cur_max = a[i]
			max_index = i
	return max_index

a_raw = [[0.0, 1.0, 1.0, 1.0, 0.0],
		 [1.0, 0.0, 0.0, 0.0, 1.0],
		 [1.0, 0.0, 0.0, 1.0, 1.0],
		 [1.0, 0.0, 1.0, 0.0, 1.0],
		 [0.0, 1.0, 1.0, 1.0, 0.0]]

a = np.matrix(a_raw)
w, v = np.linalg.eig(a)

print "Result:"
print v[:, find_max_index(w)]
```
Output:
```
Result:
[[ 0.45579856]
 [ 0.31921209]
 [ 0.49122245]
 [ 0.49122245]
 [ 0.45579856]]
```
In summary:
$$
\begin{array}{c|c}
\text{Node}&\text{Eigenvector Centrality} \\
\hline
1&0.45579856 \\
2&0.31921209 \\
3&0.49122245 \\
4&0.49122245 \\
5&0.45579856
\end{array}
$$

b)
Node 2 lies on a shortest path from node 1 to node 5
$$\text{Betweenness centrality of node 2} = \frac{1}{5 + 3 + 3} = \frac{1}{11}$$

Node 3 lies on a shortest path from node 1 to node 5
$$\text{Betweenness centrality of node 3} = \frac{1}{5 + 2 + 1} = \frac{1}{8}$$

c)
Number of shortest paths = 10
$$\text{Betweenness centrality of link (3, 4)} = \frac{1}{10}$$
$$\text{Betweenness centrality of link (2, 5)} = \frac{2}{10} = \frac{1}{5} $$

##Exercise 3

**Script**
```python
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
```

####a output
1 INFECTED
2 INFECTED
3 NOT INFECTED
4 NOT INFECTED
5 NOT INFECTED
6 NOT INFECTED
7 INFECTED
8 INFECTED

####b output
1 INFECTED
2 INFECTED
3 INFECTED
4 INFECTED
5 INFECTED
6 INFECTED
7 INFECTED
8 INFECTED

####**c**
The first seeding infects only the outer nodes in the network whereas the second infects the entire network.

Since the entire network will flip if and only if there does not exist a cluster of density 0.70 (1-0.30) or higher with state-0 at initialization.

In the first case, nodes 3, 4, 5, 6 form a cluster of density 0.75,
which matches the result obtained.

In the second case, nodes 4, 5, 6 forms a cluster of 0.5 instead,
Therefore, the entire network could flip.


##Exercise 4

```python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

s0 = 0.9
i0 = 0.1
r0 = 0

beta = 1
gamma = 1/3
nu = 1/50

def dS(s, i, r, beta, gamma, nu):
    return -beta * s * i + nu * r

def dI(s, i, r, beta, gamma, nu):
    return beta * s * i - gamma * i

def dR(s, i, r, beta, gamma, nu):
    return gamma * i - nu * r

def step_through(s0, i0, r0, beta, gamma, nu):
    s, i, r = s0, i0, r0
    s_array = [s0]
    i_array = [i0]
    r_array = [r0]
    t_array = [0]
    for t in xrange(200):
        newS = s + dS(s, i, r, beta, gamma, nu)
        newI = i + dI(s, i, r, beta, gamma, nu)
        newR = r + dR(s, i, r, beta, gamma, nu)
        s, i, r = newS, newI, newR
        s_array.append(s)
        i_array.append(i)
        r_array.append(r)
        t_array.append(t + 1)
        print "t={0} \t\ts={1} \t\ti={2} \t\tr={3}".format(round(t, 2), round(s, 2), round(i, 2), round(r, 2))
    plt.plot(t_array, s_array)
    plt.plot(t_array, r_array)
    plt.plot(t_array, i_array)
    plt.show()

'''
The values of each population fluctuate but eventually tend to constant values.
This makes sense as each 'person' can transit from r to s to i and back to r,
meaning that they will not accumulate in a certain segment of the populations S,I or R.
'''
step_through(s0, i0, r0, beta, gamma, nu)
```

> Written with [StackEdit](https://stackedit.io/).
