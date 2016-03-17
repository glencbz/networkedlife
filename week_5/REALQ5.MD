##Real Exercise 5

```python
from __future__ import division
import numpy as np

x = np.matrix([[0,1/4,1/2],[1/4,0,1/4],[1/2,1/4,0]])
e = np.matrix([[0,1,0],[1,0,0],[0,0,0]])
# print e[0]
a = np.ones([3,3])
for i in range(3):
	for j in range(3):
		if i == j:
			a[i][i] += sum(x[i].tolist()[0])
		else:
			eij = e[i].tolist()[0][j]
			xij = x[i].tolist()[0][j]
			a[i][j] -= eij*xij

# print a
C = np.linalg.inv(a)
T = np.matrix.trace(C)
N = 3
CI = []
for i in range(len(C)):
	row = C[i]
	R = sum(row)
	cc = row[i]
	information_centrality = float(1)/(cc + float(T-2*R)/N)
	CI.append(information_centrality)
print CI
```

From above example code, the information centrality of a node i, increases whenever the link containing node i increases. The change in value of the information centrality is also greater when there is no direct edge between the nodes.

From intuition, the information centrality measures importance of a node by the amount of information a node is able to deliver/receive to other nodes. If a node is able to deliver/receive information over nodes not connected directly, this would also imply greater importance for the node.
