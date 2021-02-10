key = []
val = []
m1 = {}
m2 = {}
n = int(input())
for i in range(n):
    str1,str2 = input().split()
    # print(str1,str2,sep=' ')
    m1[str1]=str2
    m2[str2]=str1
w = input()
if w in m1.keys():
    print(m1[w])
else : print(m2[w])
