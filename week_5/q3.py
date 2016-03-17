import numpy
from numpy import linalg as LA


A = [[0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0]]

A_mat = numpy.matrix(A)
w,v = LA.eig(A_mat)
print w
print v
print [row[0] for row in v.tolist()]
