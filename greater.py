a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
	larg=a
if b>a and b>c:
	larg=b
if c>a and c>b:
	larg=c
print(larg)	
