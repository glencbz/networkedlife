#!/usr/bin/python
#

from __future__ import division
import numpy as np


def generate_error_matrix(actual_matrix, pred_matrix):
	error_matrix = actual_matrix - pred_matrix
	shape = actual_matrix.shape
	for i in shape[0]:
		for j in shape[1]:
			if actual_matrix[i, j] == -1.0:
				error_matrix[i, j] = -1e99
	return error_matrix


def compute_distance(r1, r2):
	r1_valid = []
	r2_valid = []
	if r1.shape != r2.shape:
		raise Exception("computer_distance: Input shapes do not match.")
	for i in range(r1.shape[0]):
		left = r1[i, 0]
		right = r2[i, 0]
		if left != -1e99 and right != -1e99:
			r1_valid.append([left])
			r2_valid.append([right])
	r1_m = np.matrix(r1_valid)
	r2_m = np.matrix(r2_valid)
	top = r1_m.T * r2_m
	bottom = np.linalg.norm(r1_m) * np.linalg.norm(r2_m)
	return top / bottom


def neighbourhood_predict(actual_matrix):
	pass
