#queue reconstruction by height

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print("initial: ", people)
people.sort(reverse=True, key=lambda x: (x[0], -x[1]))
# reverse = true means order is from high to low.
# key means sort by what. for example sorted by the second value of element x
# then we do key=lambda x: x[1], here x is every element in people
# here we want first element of x sored from high to low, second from low to high
# so we do x:(x[0](high to low), -x[1](x[0] is high to low, but with negative sign, it becomes low to high

print("sorted: ", people)
# create an empty list
res = []
res.append(people[0])
#now we insert elements from people to res
for i in range(1, len(people)):
    current = people[i]
    num = current[1]
    res.insert(num, people[i])
print("result: ", res)







