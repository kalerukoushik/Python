

n = int(input())
for i in range(n):
    m = int(input())
    miss = []
    arr=[]
    for j in range(m):
        li = input()
        arr.append(li)
    for k in range(m):
        if k not in arr:
            print(k)
