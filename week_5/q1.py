import numpy

A = numpy.matrix([[0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]])

A2 = A * A
A3 = A2 * A
print A2
print A3