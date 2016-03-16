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