# -*- coding:utf8 -*-
# author: guoyuan
# date: 2018/03/30

# 求 1~N中，数字x (0~9) 出现的次数。 比如 1~2593中数字 5 出现的次数，注意对于555而言，数字5算出现3次。

import unittest


def count_decimal_digital_in_num_seq(N, x):
    # 排除暴力计算方式，分析题目数学特性求解
    # 函数f(abc, x)表示1 ~ abc中x出现的次数
    # 则 f(abc, x) = x出现在个位的次数 + x不出现在个位的次数
    # x出现在个位的次数 = (1 ~ ab)x 中合法的数值 + (1 ~ 9)中是否出现x
    #                 = ab - (0 if c >= x else 1) + (1 ~ 9)中是否出现x
    # x不出现在个位的次数 = f(ab-1, x) * 10 + count(ab, x) * (c + 1)
    #                   = (1 ~ ab-1)中x出现的次数 * 10 + ab中x出现的次数 * count([0 ~ c])

    if N < 9:
        return 1 if N >= x and x != 0 else 0

    N, M = divmod(N, 10)
    fisrt_part = N - (0 if M >= x else 1) + (1 if x != 0 else 0)
    second_part = count_decimal_digital_in_num_seq(N-1, x) * 10 + _count_x(N, x) * (M + 1)
    return fisrt_part + second_part

def _count_x(N, x):
    count = 0
    x = str(x)
    for n in str(N):
        count += (1 if n == x else 0)
    return count

def count_x_with_brutal_force(N, x):
    count = 0
    x = str(x)
    for i in range(1, N + 1):
        count += _count_x(i, x)

    # print("\ncount_x_with_big_force N = %d, x = %s, count = %d \n" % (N, x, count))
    return count


class TestSuite(unittest.TestCase):
    def test_lt_9(self):
        assert count_decimal_digital_in_num_seq(7, 2) == count_x_with_brutal_force(7, 2)
        assert count_decimal_digital_in_num_seq(7, 8) == count_x_with_brutal_force(7, 8)

    def test_9_and_99(self):
        assert count_decimal_digital_in_num_seq(10, 0) == count_x_with_brutal_force(10, 0)
        assert count_decimal_digital_in_num_seq(11, 1) == count_x_with_brutal_force(11, 1)
        assert count_decimal_digital_in_num_seq(99, 4) == count_x_with_brutal_force(99, 4)

    def test_99_and_999(self):
        assert count_decimal_digital_in_num_seq(999, 0) == count_x_with_brutal_force(999, 0)
        assert count_decimal_digital_in_num_seq(999, 9) == count_x_with_brutal_force(999, 9)
        assert count_decimal_digital_in_num_seq(302, 2) == count_x_with_brutal_force(302, 2)

    def test_common(self):
        assert count_decimal_digital_in_num_seq(2593, 0) == count_x_with_brutal_force(2593, 0)
        assert count_decimal_digital_in_num_seq(2593, 1) == count_x_with_brutal_force(2593, 1)
        assert count_decimal_digital_in_num_seq(2593, 5) == count_x_with_brutal_force(2593, 5)

if __name__ == '__main__':
    unittest.main()
