k1 = [2, 4, 3]
k2 = [5, 6, 4]


# list[start:stop:step]

def addTwoNumbers(l1, l2):
    # list[start:stop:step]
    reversed_l1 = l1[::-1]
    reversed_l2 = l2[::-1]

    res_1 = int("".join(map(str, reversed_l1)))
    res_2 = int("".join(map(str, reversed_l2)))

    result = 0

    result = res_1 + res_2

    res_3 = list(map(int, str(result)))
    reversed_res_3 = res_3[::-1]

    return reversed_res_3


print(addTwoNumbers(k1, k2))