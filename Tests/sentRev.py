def sentRev():
    s = input()
    print('.'.join(s.split('.')[::-1]))
	
n =int(input())
for i in range(n):
    sentRev()
