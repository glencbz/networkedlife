from __future__ import division
import numpy

N = 2
# N = 3
H_LIST = [[1,0],[1/3, 2/3]]
# H_LIST = [[0,1],[1,0]]
# H_LIST = [[1/2, 0, 1/2],[1/2,0,1/2],[1/3,1/3,1/3]]
THRESHOLD = 1E-40

H = numpy.matrix(H_LIST)
G = 0.85*numpy.matrix(H_LIST) + 0.15/N*numpy.ones((N,N))
print G
pi_start = 1/N * numpy.ones((1,N)) * G
pi_old = pi_start
pi_new = pi_old*G
count = 1

while abs(numpy.sum(pi_old - pi_new)) > THRESHOLD:
	pi_old = pi_new
	pi_new = pi_old * G
	count+=1

print count, pi_new
