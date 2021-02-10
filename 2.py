a = set()
b = set()
aa = []
bb = []
aa = [int(i) for i in input().split()]
for i in aa:
    a.add(i)
bb = [int(i) for i in input().split()]
for i in bb:
    b.add(i)
c = a.intersection(b)
print(len(c))