l=int(input())
u=int(input())
for num in range (l,u+1):
	sum=0
	temp=num
	while temp>0:
		dig=temp%10
		sum+=dig**3
		temp//=10
	if num==sum:
		print(num)
