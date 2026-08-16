# -*- coding:utf8 -*-
# author: guoyuan
# date: 2018/03/29

# 有一个m*n整数矩阵，从左到右单调递增，从上到下单调递增，判断一个指定的数是否在此矩阵中？
# 求 1~N中，数字x (0~9) 出现的次数。 比如 1~2593中数字 5 出现的次数，注意对于555而言，数字5算出现3次。

import bisect


def check_if_num_in_matrix(matrix, num):
    # matrix in python
    # m=2 * n=3 [[1, 3, 5], [7, 9, 11]]
    # O(m + lgm + m + n + lgn)

    if not matrix:
        return False

    row_right = [row[-1] for row in matrix]

    # binary search
    point = bisect.bisect_left(row_right, num)

    if point >= len(row_right):
        return False

    else:
        check_row = matrix[point]
        # binary search
        point = bisect.bisect_left(check_row, num)

        if point >= len(check_row):
            return False

        else:
            return check_row[point] == num


if __name__ == '__main__':
    matrix = [[1, 3, 5], [7, 9, 11]]
    print(check_if_num_in_matrix(matrix, num=4))  # False
    print(check_if_num_in_matrix(matrix, num=5))  # True
    print(check_if_num_in_matrix(matrix, num=11))  # True
    print(check_if_num_in_matrix(matrix, num=12))  # False
    print(check_if_num_in_matrix(matrix, num=6))  # False
