cnt = []
# st = {}
for i in range(0,100001):
    cnt.append(0)
a = [int(i) for i in input().split()]
for i in a:
    cnt[i]+=1
ans = 0
for i in cnt:
    if i != 0:
        ans += 1
print(ans)