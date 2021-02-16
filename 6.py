d = {}
try:
    while True:
        a = input().split()
        # print(a)
        for s in a:
            if d.get(s, 0) != 0:
                d[s] += 1
            else: d[s] = 1
except:
    pass
def f(p):
    return (-p[1], p[0])
for i in sorted(d.items(), key=f):
    print(i[0])
