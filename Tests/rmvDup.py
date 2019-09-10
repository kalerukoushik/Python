def removeDup():
    s = input()
    s1 = []
    for i in range(0, len(s)):
        if s[i]!=s[i+1]:
            s1.append(s[i])
        
    return s1
        

n = int(input())
s1 = []
for i in range(n):
    s2 = removeDup()
    
print('\n'.join(s2))
