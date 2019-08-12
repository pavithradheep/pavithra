low=int(input())
hig=int(input())
for num in range (low,hig+1):
	sum=0
	temp=num
	while temp>0:
		dig=temp%10
		sum+=dig**3
		temp//=10
	if num==sum:
		print(num)
