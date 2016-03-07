from __future__ import division
import numpy

N = 5
H_LIST = [[0, 1, 0, 0, 0],
	[1, 0, 0, 0, 0],
	[1/3, 0, 1/3, 0, 1/3],
	[0, 0, 1/2, 0, 1/2],
	[0, 0, 0, 0, 0]]

ZERO_ROW = numpy.matrix([0, 0, 0, 0, 1]).T
THETAS = [0.1, 0.3, 0.5, 0.85]
THRESHOLD = 1E-40
START = 1/N * numpy.ones(5)

H = numpy.matrix(H_LIST)
H_hat = H + (1/N) * ZERO_ROW * numpy.ones(5)

for theta in THETAS:
	print "theta = " + str(theta)
	G = theta * H_hat + (1 - theta) * (1/N) * numpy.ones((5, 5))
	pi_old = START * G
	pi_new = pi_old * G
	counter = 0
	while abs(numpy.sum(pi_old - pi_new)) > THRESHOLD:
		pi_old = pi_new
		pi_new = pi_old * G
		counter += 1
	pi_list = pi_new[0].tolist()[0]
	print "pi = " + str([round(el, 3) for el in pi_list])
	sorted_pi_list = sorted(list(enumerate(pi_list)), key=lambda x: x[1], reverse=True)
	print "ranking = " + str([el[0] + 1 for el in sorted_pi_list])
	print "--------------------\n"
