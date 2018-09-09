"""
791 custom sort string
"""


def custom_sort_string(S, T):
    """

    :param S: str
    :param T: str
    :return: str
    """
    order = []
    for i in range (len(S)):
        element = []
        element.append(S[i])
        element.append(i)
        order.append(element)
    for j in range(len(T)):
        if T[j] in S:
            order[S.index(T[j])].append(T[j])
        else:
            order.append(T[j])
    result = ""
    for z in range(len(S)):
        result += ''.join(order[z][2:])
    result += ''.join(order[len(S):])
    return result


S = "cba"
T = "abdjhaaacc"
print(custom_sort_string(S, T))