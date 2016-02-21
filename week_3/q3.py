from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# Minimise ||Ab - c||^2_2

# A - 4 by 3 matrix
# B - 3 by 1 matrix
# C - 4 by 1 matrix

A = [[1,0,2],
	[1,1,0],
	[0,2,1],
	[2,1,1]]

C = [[2],
	[1],
	[1],
	[3]]

A = np.matrix(A)
C = np.matrix(C)

ATA = np.transpose(A) * A
ATAinv = np.linalg.inv(ATA)

ATC = np.transpose(A) * C
B = ATAinv * ATC

print B

reg_factors = np.arange(0,5.2,0.2)
b_list = []

for lamda in reg_factors:
	ATAinv = np.linalg.inv(ATA + (lamda*np.eye(3)/2))
	b_list.append(ATAinv * ATC)

abcl2 = [float(np.transpose(A*b - C) * (A*b - C)) for b in b_list]
bl2 = [float(np.transpose(b) * (b)) for b in b_list]

plt.plot(reg_factors, abcl2)
plt.plot(reg_factors, bl2)
plt.legend(['(Ab - c)^T(Ab - c)', 'b^T*b'])
plt.show()
