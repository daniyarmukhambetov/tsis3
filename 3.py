a = set()
b = set()
aa = []
bb = []
aa = [int(i) for i in input().split()]
for i in aa:
    a.add(i)
bb = [int(j) for j in input().split()]
for j in bb:
    b.add(j)
c = a.intersection(b)
for cc in c:
    print(cc,end=' ')