#/usr/bin/python
#

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

