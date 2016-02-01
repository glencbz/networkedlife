###Exercise 2. Power control infeasibility

#####Consider a three-link cell with the link gains $G_{ij}$ shown below. The receivers request $\gamma_1 = 1, \gamma_2 = 2, \gamma_3 = 1$. The noise $n_i =0.1$ for all $i$.
$$G = \begin{pmatrix}1&0.5&0.5\\0.5&1&0.5\\0.5&0.5&1\end{pmatrix}$$

#####Show this set of target SIRs is infeasible.

Using the SIR formula,

$$SIR_i = \frac{G_{ii}p_i}{\sum_{j\neq i }G_{ij}p_j + n_i}$$

We have 
$$SIR_1 = \frac{p_1}{0.5p_2 + 0.5p_3 + 0.1} \ge 1 \\ SIR_2 = \frac{p_2}{0.5p_1 + 0.5p_3 + 0.1} \ge 2 \\ SIR_3 = \frac{p_3}{0.5p_1 + 0.5p_2 + 0.1} \ge 1$$

Rearranging the terms, we get the following linear problem,

$$\begin{bmatrix}p_1&-0.5p_2&-0.5p_3
\\-p_1&p_2&-p_3
\\-0.5p_1&-0.5p_2&p_3&
\end{bmatrix} \ge \begin{bmatrix} 0.1\\0.2\\0.1
\end{bmatrix}$$

Solving the linear problem,

r2 = r2 + r1
r3 = r3*2 + r1

$$\begin{bmatrix}p_1&-0.5p_2&-0.5p_3
\\0&0.5p_2&-1.5p_3
\\0&-1.5p_2&1.5p_3&
\end{bmatrix} \ge \begin{bmatrix} 0.1\\0.3\\0.3
\end{bmatrix}$$

r1 = r1 + r2
r2 = 2*r2
r3 = r3 + 1.5*r2

$$\begin{bmatrix}p_1&0&-2p_3
\\0&p_2&-3p_3
\\0&0&-3p_3&
\end{bmatrix} \ge \begin{bmatrix} 0.4\\0.6\\1.2
\end{bmatrix}$$

r3 = r3 / -3
r2 = r2 + 3*r3
r1 = r1 + 2*r3

$$\begin{bmatrix}p_1&0&0
\\0&p_2&0
\\0&0&p_3&
\end{bmatrix} \le \begin{bmatrix} -0.4\\-0.6\\-0.4
\end{bmatrix}$$

Since the power values are negative, this implies that the problem is infeasible. 
