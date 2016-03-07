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

# Solving for A^T*A
ATA = np.transpose(A) * A

# Solving for (A^T*A)^(-1)
ATAinv = np.linalg.inv(ATA)

# Solving for A^T*c
ATC = np.transpose(A) * C

# Solving for b
B = ATAinv * ATC

print B

# Generating list of regularization factors
reg_factors = np.arange(0,5.2,0.2)
b_list = []

# Iterating through all lambda from 0.2 to 5.0
for lamda in reg_factors:
    
    # Calculating inverse for (2 A^T * A + lambda/2)
	ATAinv = np.linalg.inv(ATA + (lamda*np.eye(3)/2))
    
    # Calculating b values
	b_list.append(ATAinv * ATC)

# Calculating list for ||Ab - c||^2_2
abcl2 = [float(np.transpose(A*b - C) * (A*b - C)) for b in b_list]
# Calculating list for ||b||^2_2
bl2 = [float(np.transpose(b) * (b)) for b in b_list]

# print b_list

plt.title("Plot of $(Ab - c)^T(Ab - c)$ and $b^Tb$ against $\lambda$")
plt.plot(reg_factors, abcl2)
plt.plot(reg_factors, bl2)
plt.legend(['$(Ab - c)^T(Ab - c)$', '$b^Tb$'])
plt.show()
