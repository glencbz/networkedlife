#Networked Life HW 6

#####Glen Choo 1000472
#####Loo Juin 1000546
#####Tan Hao Qin 1000521

##Question 1

$$
\begin{array}{c|cccccc}
\text{Node}&1&2&3&4&5&6 \\
\hline
t = 0&0&\infty&\infty&\infty&\infty&\infty \\
t = 1&0&4&1&5&\infty&8 \\
t = 2&0&4&1&5&6&7 
\end{array}
$$

##Question 2

**1**
Without statistical multiplexing, one assumes that all users are busy all the time. $N_d$ is thus the maximum value of $N$ that satisfies $N <= C$, i.e. $N_d = C$.

**2**

Since $N_d = C$,
$$P(X > C) < \gamma$$

Using
$$
\begin{align}
P(X > C) &= 1 - P(X \le C)\\
&= 1 - (\sum^C_{i=0}p^i(1 - p)^{N_s - i}
\begin{pmatrix}N_s\\i\end{pmatrix})
\end{align}
$$

We select the highest value of $N_s$ that satisfies this relationship.

Given $p = 0.1, \gamma = 0.01$,
for $C = 10,20,30$, $N_s = 50,  122, 301$. Thus $N_s$ grows more quickly than $C$ and a link of $2C$ accommodates more than $2N_s$ users.

$\sum^{N_s}_{i= N_d +1}P(X = i)$ is the probability that the link is congested.

**3**

For a link of capacity $2C$, $N_{s2} > 2N_s$. This is greater than two links of capacity, $C$ which can accommodate $N_s + N_s = 2N_s$.

```import math

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def pXC(Ns, k, p):
    return (p ** k) * ((1- p) ** (Ns - k)) * nCr(Ns, k)

def pXgeC(Ns, C, p):
    p_masses = tuple(pXC(Ns, i, p) for i in range(0, C+1))
    return 1 - sum(p_masses)

def computeNs(C, p, gamma):
    ns = C
    while True:
        if pXgeC(ns, C, p) > gamma:
            break
        ns += 1
    return ns - 1

for i in [10,20,30]:
    print computeNs(i, 0.1, 0.01)
	# 50, 122, 200
```


##Question 3

$$E[n,p] = \frac{\frac{p^n}{n!}}{}$$

Sub $tp = p$ into Equation 1

$$e^{-t\rho}\sum^n_{k=0} (t\rho)^k / k! = \int^\infty_{tp}\frac{x^ne^{-x}}{n!}dx$$

Sub $t\rho = \rho, tn = n$ into $1/E[n,\rho]$


$$\frac{1}{E[tn,t\rho]} = \frac{\sum^{tn}_{i=0}\frac{t\rho^i}{i!}}{\frac{(t\rho)^n}{(tn)!}} \\
=\frac{(tn)!}{(t\rho)^n}e^{t\rho}\int^\infty_{tp}\frac{x^{tn}e^{-x}}{(tn)!}dx
\\=\frac{(tn)!}{(t\rho)^n}\frac{1}{(tn)!}e^{t\rho}\int^\infty_{tp}x^{tn}e^{-x}dx
\\=\frac{e^{t\rho}}{(t\rho)^n}\int^\infty_{tp}x^{tn}e^{-x}dx$$

Reindex $t\rho$ to 0

$$\frac{1}{E[tn,t\rho]}=\frac{e^{t\rho}}{(t\rho)^n}\int^\infty_0x^{tn}e^{-x}dx$$

Integrating $x^{tn}e^{-x}$, we get

$$\frac{1}{E[tn,t\rho]}=\frac{e^{t\rho}}{(t\rho)^n}\Gamma(tn + 1)$$

Since an exponential function increases at a far greater rate than a polynomial function, $\frac{e^{t\rho}}{(t\rho)^n}$ is an increasing function.

Since the gamma function is an increasing function as well, this implies that $\frac{1}{E[tn,t\rho]}$ is an increasing function as well.

As such, $E[tn,t\rho]$ is a strictly decreasing function in $t$, which implies that $E[2n,2ρ] < E[n,ρ]$.

> Written with [StackEdit](https://stackedit.io/).