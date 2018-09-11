a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
b = a[:]
import math
class Solution(object):
    def totalrec(self, b):
        totalrec = 0
        for i in range(len(b) - 1):
            current = b[i]
            for k in range(len(b) - 1 - i):
                compare = b[k]
                count = 0
                for j in range(len(b[0])):
                    if current[j] & compare[j] == 1:
                        count += 1
                count1 = count - 1
                totalrec += ((1 + count1) * count1) // 2
        return totalrec

mysol =  Solution()
print(mysol.totalrec(b))


