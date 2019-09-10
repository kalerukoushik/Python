def rmvDup(s):
    for i, (curr, nxt) in enumerate(zip(s, s[1:])):
        if curr == nxt:
            return(s[:i] + rmvDup(s[i+1:]))
    return s

n = int(input())
s1 = []
for i in range(n):
    s = input()
    s1.append(rmvDup(s))
print('\n'.join(s1))
