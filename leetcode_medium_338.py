def count_bits(num):
    l = []
    for i in range(num+1):
        count = bin(i)[2:].count('1')
        l.append(count)
    return l


print(count_bits(5))


