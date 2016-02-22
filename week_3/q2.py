#!/usr/bin/python
#

from __future__ import division
import numpy as np
from q1 import *


INFINITY_VALUE = 100000


def generate_error_matrix(actual_matrix, pred_matrix):
	error_matrix = actual_matrix - pred_matrix
	shape = actual_matrix.shape
	for i in range(shape[0]):
		for j in range(shape[1]):
			if actual_matrix[i, j] == -1:
				error_matrix[i, j] = -INFINITY_VALUE
	return error_matrix


def compute_distance(r1, r2):
	if r1.shape != r2.shape:
		raise Exception("compute_distance: Input shapes do not match.")
	numerator = 0.0
	r1_summer = 0.0
	r2_summer = 0.0
	for i in range(r1.shape[0]):
		left = r1[i, 0]
		right = r2[i, 0]
		if left != -INFINITY_VALUE and right != -INFINITY_VALUE:
			numerator += left * right
			r1_summer += left ** 2
			r2_summer += right ** 2
	return numerator / np.sqrt(r1_summer * r2_summer) if r1_summer != 0 and r2_summer != 0 else 0


class DistanceMachine:
	def __init__(self, error_matrix):
		self.error_matrix = error_matrix
		self.struct = {}

	def get(self, a, b):
		index = (a, b) if b >= a else (b, a)
		try:
			return self.struct[index]
		except KeyError:
			dist = compute_distance(self.error_matrix[:, a], self.error_matrix[:, b])
			# print "Dist (%d, %d):" % (a, b), dist
			self.struct[index] = dist
			return dist


class NeighbourhoodMachine:
	def __init__(self, error_matrix, size):
		if size >= error_matrix.shape[1]:
			raise Exception("NeighbourhoodMachine: Cannot have neighbourhood size equal to or larger than number of movies!")
		self.error_matrix = error_matrix
		self.size = size
		self.dist_machine = DistanceMachine(error_matrix)
		self.struct = {}

	def get(self, i):
		try:
			return self.struct[i]
		except KeyError:
			dists = []
			for j in range(self.error_matrix.shape[1]):
				if j != i:
					dists.append((j, self.dist_machine.get(i, j)))
			dists = sorted(dists, key = lambda k: -np.abs(k[1]))
			# print i, dists
			self.struct[i] = dists[0:self.size]
			return self.struct[i]


def neighbourhood_predict(actual_matrix, pred_matrix, size):
	error_matrix = generate_error_matrix(actual_matrix, pred_matrix)
	nbh_machine = NeighbourhoodMachine(error_matrix, size)
	ret_matrix = np.matrix([[0.0] * pred_matrix.shape[1]] * pred_matrix.shape[0])
	for u in range(pred_matrix.shape[0]):
		for i in range(pred_matrix.shape[1]):
			nbh = nbh_machine.get(i)
			numerator = 0.0
			denominator = 0.0
			for n in nbh:
				if error_matrix[u, n[0]] != -INFINITY_VALUE:
					numerator += n[1] * error_matrix[u, n[0]]
					denominator += np.abs(n[1])
			offset = numerator/denominator
			ret_matrix[u, i] = pred_matrix[u, i] + offset
	return ret_matrix


if __name__ == "__main__":
	actual_matrix = np.matrix([[5, 4, 4, -1, 5],
							   [-1, 3, 5, 3, 4],
							   [5, 2, -1, 2, 3],
							   [-1, 2, 3, 1, 2],
							   [4, -1, 5, 4, 5],
							   [5, 3, -1, 3, 5],
							   [3, 2, 3, 2, -1],
							   [5, 3, 4, -1, 5],
							   [4, 2, 5, 4, -1],
							   [5, -1, 5, 3, 4]])
	print "Actual ratings:"
	print actual_matrix
	pred_matrix = np.matrix([[5.0, 3.09, 4.90, -1, 4.62],
							 [-1, 2.89, 4.69, 3.49, 4.42],
							 [4.1, 2.19, -1, 2.78, 3.71],
							 [-1, 1.0, 2.49, 1.29, 2.22],
							 [4.9, -1, 4.79, 3.58, 4.51],
							 [4.88, 2.96, -1, 3.56, 4.48],
							 [3.15, 1.23, 3.03, 1.82, -1],
							 [4.84, 2.92, 4.72, -1, 4.44],
							 [4.84, 2.92, 4.72, 3.51, -1],
							 [4.61, -1, 4.49, 3.29, 4.22]])
	print "Predicted ratings:"
	print pred_matrix
	offset_matrix = neighbourhood_predict(actual_matrix, pred_matrix, 2)
	print "New predictions:"
	print offset_matrix
