
#Networked Life

#####Glen Choo 1000472
#####Loo Juin 1000546
#####Tan Hao Qin 1000521

###Exercise 1

####Python code
```python
import matplotlib.pyplot as plotter


noise = 0.1


def sir(id, state, gain_matrix):
	numerator = gain_matrix[id][id] * state[id]
	denominator = 0.0
	for i in range(len(state)):
		if i != id:
			denominator += ((gain_matrix[id][i] * state[i]) + noise)
	return numerator / denominator


def dpc_iterate(id, previous_state, gammas, gain_matrix):
	return (gammas[id] / sir(id, previous_state, gain_matrix)) * previous_state[id]


def run_iterations(n, init_state, gammas, gain_matrix):
	states = [init_state]
	for i in range(n):
		new_state = []
		for j in range(len(states[-1])):
			new_state.append(dpc_iterate(j, states[-1], gammas, gain_matrix))
		states.append(new_state)
	return states


def extract_column(states, id):
	return [i[id] for i in states]


if __name__ == '__main__':
	G = [[1.0, 0.1, 0.3],
		 [0.2, 1.0, 0.3],
		 [0.2, 0.2, 1.0]]
	gammas = [1.0, 1.5, 1.0]
	init_state = [1.0, 1.0, 1.0]
	num_iter = 10

	states = run_iterations(num_iter, init_state, gammas, G)
	x_axis = range(len(states))
	plotter.plot(x_axis, extract_column(states, 0), "ro-")
	plotter.plot(x_axis, extract_column(states, 1), "go-")
	plotter.plot(x_axis, extract_column(states, 2), "bo-")
	plotter.show()
	print "Part 1 Done"

	new_init_state = []
	for state in states[-1]:
		new_init_state.append(state)
	new_init_state.append(1.0)
	new_gammas = [1.0, 1.5, 1.0, 1.0]
	new_G = [[1.0, 0.1, 0.3, 0.1],
			 [0.2, 1.0, 0.3, 0.1],
		 	 [0.2, 0.2, 1.0, 0.1],
			 [0.1, 0.1, 0.1, 1.0]]

	new_states = run_iterations(num_iter, new_init_state, new_gammas, new_G)
	x_axis = range(len(states))
	plotter.plot(x_axis, extract_column(new_states, 0), "ro-")
	plotter.plot(x_axis, extract_column(new_states, 1), "go-")
	plotter.plot(x_axis, extract_column(new_states, 2), "bo-")
	plotter.plot(x_axis, extract_column(new_states, 3), "yo-")
	plotter.show()
	print "Part 2 Done"
```

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

###Exercise 3

For the row player, choosing $b$ dominates choosing $a$, whereas for the column player, choosing $a$ dominates choosing $b$. The pure strategy equilibirum would thus be $(b,a)$.

###Exercise 4
**a**
![](https://raw.githubusercontent.com/glencbz/networkedlife/master/week_1/4a.png)
**b**
$$
\begin{array}{c|ccc}
 &1&2&3\\
 \hline
1&-\infty, -1&-2, -\infty&-3, -\infty\\
2&-2,-\infty&-\infty, -2&-\infty, -3\\
3&-3,-\infty&-3,-2&-2,-\infty\\
\end{array}
$$

**c**
3,2

> Written with [StackEdit](https://stackedit.io/).