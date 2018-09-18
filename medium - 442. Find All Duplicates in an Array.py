"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""
a = [4,3,2,7,8,2,3,1]
def find_duplicates (a):
    """

    :param a: list[int]
    :return: list[int]
    """
    non_duplicate = []
    res = []
    for i in range(len(a)):
        if a[i] in non_duplicate:
            res.append(a[i])
        else:
            non_duplicate.append(a[i])
    return res

print(find_duplicates(a))
