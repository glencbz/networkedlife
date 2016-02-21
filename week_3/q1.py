from __future__ import division
import numpy as np

R_LIST = [[5,-1,5,4], [-1,1,1,4], [4,1,2,4],[3,4,-1,3], [1,5,3,-1]]
FLOAT_R_LIST = [map(lambda x: float(x), row) for row in R_LIST]
R = np.matrix(FLOAT_R_LIST)

def build_A(R_list):
	A = []
	A_row_length = len(R_LIST) + len(R_LIST[0])
	movie_base = len(R_LIST)
	for user_index in range(len(R_LIST)):
		for movie_offset in range(len(R_LIST[user_index])):
			movie_index = movie_offset + movie_base
			if R_LIST[user_index][movie_offset] > 0:
				A.append(build_A_row(A_row_length,user_index,movie_index))
	return A

def build_A_row(length,i,j):
	return [1 if x is i or x is j else 0 for x in range(length)]

def build_c(R_LIST):
	ratings = []
	for row in R_LIST:
		for ele in row:
			if ele > 0:
				ratings.append(ele)
	average = sum(ratings)/len(ratings)
	return [ele - average for ele in ratings]

def solve_b(A_list, c_list):
	A = np.matrix(A_list)
	c = np.matrix(c_list).T
	return np.linalg.inv(A.T * A) * A.T * c

def convert_b(b):
	return [ele[0] for ele in b.tolist()]

def build_R_hat(R_LIST, b_list):
	R_hat = R_LIST
	movie_base = len(R_LIST)
	ratings = []
	for user in R_LIST:
		for ele in row:
			if ele > 0:
				ratings.append(ele)
	average = sum(ratings)/len(ratings)

	movie_base = len(R_LIST)
	for user_index in range(len(R_LIST)):
		for movie_offset in range(len(R_LIST[user_index])):
			if R_hat[user_index][movie_offset] > 0:
				R_hat[user_index][movie_offset] = average + b_list[user_index] + b_list[movie_offset + movie_base]
	return np.matrix(R_hat)
if __name__ == "__main__":
	print build_R_hat(R_LIST, convert_b(solve_b(build_A(R_LIST), build_c(R_LIST))))