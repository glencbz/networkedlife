#!/usr/bin/python
#

import numpy as np

num_iter = 10

p0 = np.matrix([[0.5], [0.5], [0.0], [0.0]])

H = np.matrix([[0, 1, 0, 0],
			   [0, 0, 1, 0],
			   [0, 0, 0, 1],
			   [1, 0, 0, 0]])

pis = [p0]

for i in range(num_iter):
	new_p = pis[-1].T * H
	pis.append(new_p.T)

for i in range(len(pis)):
	cur_p = pis[i]
	print '$\\pi[%d] = \\begin{bmatrix}%.3f&%.3f&%.3f&%.3f\\end{bmatrix}^T$' % (i, cur_p[0, 0], cur_p[1, 0], cur_p[2, 0], cur_p[3, 0])