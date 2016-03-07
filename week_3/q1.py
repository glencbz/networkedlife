from __future__ import division
import numpy as np
import itertools

def build_a(r_list):
    a_list = []
    a_row_length = len(r_list) + len(r_list[0])
    movie_base = len(r_list)
    for user_index, _ in enumerate(r_list):
        for movie_offset in range(len(r_list[user_index])):
            movie_index = movie_offset + movie_base
            if r_list[user_index][movie_offset] > 0:
                a_list.append(build_a_row(a_row_length, user_index, movie_index))
    return a_list

def build_a_row(length, i, j):
    return [1 if ele is i or ele is j else 0 for ele in xrange(length)]

def build_c(r_list):
    ratings = [ele for user in r_list for ele in user if ele > 0]
    average = sum(ratings)/len(ratings)
    return [ele - average for ele in ratings]

def solve_b(a_list, c_list):
    a_mat = np.matrix(a_list)
    c_mat = np.matrix(c_list).T
    return np.linalg.inv(a_mat.T * a_mat) * a_mat.T * c_mat

def convert_b(b_mat):
    return [ele[0] for ele in b_mat.tolist()]

def build_r_hat(r_list, b_list):
    r_hat = r_list
    movie_base = len(r_list)
    ratings = [ele for user in r_list for ele in user if ele > 0]

    average = sum(ratings)/len(ratings)

    movie_base = len(r_list)
    for user_index, _ in enumerate(r_list):
        for movie_offset in xrange(len(r_list[user_index])):
            r_hat[user_index][movie_offset] = average + b_list[user_index] + \
            									b_list[movie_offset + movie_base]
    return np.matrix(r_hat)

def get_r_hat(r_list):
    return build_r_hat(r_list, convert_b(solve_b(build_a(r_list), build_c(r_list))))

if __name__ == "__main__":
    R_LIST = [[5, -1, 5, 4],
              [-1, 1, 1, 4],
              [4, 1, 2, 4],
              [3, 4, -1, 3],
              [1, 5, 3, -1]]

    FLOAT_R_LIST = [[float(x) for x in row] for row in R_LIST]
    print get_r_hat(FLOAT_R_LIST)
