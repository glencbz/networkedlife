#!~/anaconda/bin/python
#


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
