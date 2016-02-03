
#Networked Life

#####Glen Choo 1000472
#####Loo Juin 1000546
#####Tan Hao Qin 1000521

###Exercise 1

####Part a
![](https://raw.githubusercontent.com/glencbz/networkedlife/master/week_1/Q1a.png)

####Part b
![](https://raw.githubusercontent.com/glencbz/networkedlife/master/week_1/Q1b.png)


###Exercise 2. Power control infeasibility

#####Consider a three-link cell with the link gains $G_{ij}$ shown below. The receivers request $\gamma_1 = 1, \gamma_2 = 2, \gamma_3 = 1$. The noise $n_i =0.1$ for all $i$.
$$G = \begin{pmatrix}1&0.5&0.5\\0.5&1&0.5\\0.5&0.5&1\end{pmatrix}$$

#####Show this set of target SIRs is infeasible.

Using the SIR formula,

$$SIR_i = \frac{G_{ii}p_i}{\sum_{j\neq i }G_{ij}p_j + n_i}$$

We have 
$$SIR_1 = \frac{p_1}{0.5p_2 + 0.5p_3 + 0.1} \ge 1 \\ SIR_2 = \frac{p_2}{0.5p_1 + 0.5p_3 + 0.1} \ge 2 \\ SIR_3 = \frac{p_3}{0.5p_1 + 0.5p_2 + 0.1} \ge 1$$

Rearranging the terms, we get the following linear problem,

$$\begin{bmatrix}1&-0.5&-0.5
\\-1&1&-1
\\-0.5&-0.5&1
\end{bmatrix} \begin{bmatrix} p_1\\p_2\\p_3
\end{bmatrix} \ge \begin{bmatrix} 0.1\\0.2\\0.1
\end{bmatrix}$$

Solving the linear problem,

$R_2 = R_2 + R_1$
$R_3 = R_3*2 + R_1$

$$\begin{bmatrix}1&-0.5&-0.5
\\0&0.5&-1.5
\\0&-1.5&1.5
\end{bmatrix} \begin{bmatrix} p_1\\p_2\\p_3
\end{bmatrix} \ge \begin{bmatrix} 0.1\\0.3\\0.3
\end{bmatrix}$$

$R_1 = R_1 + R_2$
$R_2 = 2*R_2$
$R_3 = R_3/1.5 + R2 $

$$\begin{bmatrix}1&0&-2
\\0&1&-3
\\0&0&-2
\end{bmatrix} \begin{bmatrix} p_1\\p_2\\p_3
\end{bmatrix} \ge \begin{bmatrix} 0.4\\0.6\\0.8
\end{bmatrix}$$

$R_3 = R_3 / -2$
$R_2 = R_2 + 3*R_3$
$R_1 = R_1 + 2*R_3$

$$\begin{bmatrix}1&0&0
\\0&1&0
\\0&0&1
\end{bmatrix} \begin{bmatrix} p_1\\p_2\\p_3
\end{bmatrix} \le \begin{bmatrix} -0.4\\-0.6\\-0.4
\end{bmatrix}$$

Since the power values are negative, this implies that the problem is infeasible. 

###Exercise 3

For the row player, choosing $b$ dominates choosing $a$, whereas for the column player, choosing $a$ dominates choosing $b$. The pure strategy equilibirum would thus be $(b,a)$.

###Exercise 4
**a**
![](https://raw.githubusercontent.com/glencbz/networkedlife/master/week_1/4a.png)
**b**
$$
p_2\\
p_1 \quad
\begin{array}{c|ccc}
&1&2&3\\
 \hline
1&-\infty, -1&-\infty, -2&-\infty, -3\\
2&-2,-\infty&-\infty, -2&-\infty, -3\\
3&-3,-\infty&-3,-2&-3,-\infty\\
\end{array}
$$

**c**
3,2

> Written with [StackEdit](https://stackedit.io/).