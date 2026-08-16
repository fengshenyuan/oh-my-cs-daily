# -*-coding:utf8-*-

def bin_search(ls, a):
    # check ls type
    if not isinstance(ls, (list, tuple)):
        return -1

    ls_len = len(ls)
    # check ls elem
    if ls_len == 0:
        return -1

    # check 1 or 2 elem conditions
    if ls_len == 1:
        if a == ls[0]:
            return 0

        else:
            return -1

    half = int(ls_len / 2)

    ck = ls[half]
    if ck == a:
        return half

    if ck < a:
        return bin_search(ls[half + 1:], a)

    else:
        return bin_search(ls[:half], a)

if __name__ == '__main__':
    x = [1, 2, 4, 6, 10, 29, 30]
    pos = bin_search(ls=x, a=1)
    print("pos = ", pos)
