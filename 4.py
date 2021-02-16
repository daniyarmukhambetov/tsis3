n, m = [int(i) for i in input().split()]
a = set()
b = set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
print(len(a.intersection(b)))
for i in a.intersection(b):
    print(i, end = ' ')
print()
print(len(a.difference(b)))
for i in a.difference(b):
    print(i, end = ' ')
print()
print(len(b.difference(a)))
for i in b.difference(a):
    print(i, end = ' ')
# print('\n')