#!/usr/bin/python
#

from __future__ import division
import numpy as np
from q1 import *


INFINITY_VALUE = 1000


def generate_error_matrix(actual_matrix, pred_matrix):
	error_matrix = actual_matrix - pred_matrix
	shape = actual_matrix.shape
	for i in range(shape[0]):
		for j in range(shape[1]):
			if actual_matrix[i, j] == -1.0:
				error_matrix[i, j] = -INFINITY_VALUE
	return error_matrix


def compute_distance(r1, r2):
	r1_valid = []
	r2_valid = []
	if r1.shape != r2.shape:
		raise Exception("compute_distance: Input shapes do not match.")
	for i in range(r1.shape[0]):
		left = r1[i, 0]
		right = r2[i, 0]
		if left != -1000 and right != -1000:
			r1_valid.append([left])
			r2_valid.append([right])
	r1_m = np.matrix(r1_valid)
	r2_m = np.matrix(r2_valid)
	top = float(r1_m.T * r2_m)
	bottom = float(np.linalg.norm(r1_m) * np.linalg.norm(r2_m))
	return top / bottom if bottom != 0 else INFINITY_VALUE


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
					dists.append((i, self.dist_machine.get(i, j)))
			dists = sorted(dists, key = lambda k: k[1])
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
				numerator += n[1] * error_matrix[u, i]
				denominator += np.abs(n[1])
			offset = numerator/denominator
			ret_matrix[u, i] = pred_matrix[u, i] + offset
	return ret_matrix

if __name__ == "__main__":
	actual_matrix = np.matrix([[5, -1, 5, 4], [-1, 1, 1, 4], [4, 1, 2, 4],[3, 4, -1, 3], [1, 5, 3, -1]])
	print "Actual ratings:"
	print actual_matrix
	pred_matrix = np.matrix([[3, 5, 3, 4], [3, 5, 1, 3], [3, 3, 2, 5], [1, 1, 4, 5], [2, 5, 3, 1]])
	print "Predicted ratings:"
	print pred_matrix
	offset_matrix = neighbourhood_predict(actual_matrix, pred_matrix, 2)
	print "New predictions:"
	print offset_matrix
