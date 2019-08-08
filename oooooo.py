number=int(input())
temp=number
rev=0
while temp!=0:
	rev=(rev*10)+(temp%10)
	temp=temp//10
if number==rev:
	print("yes")
else:
	print("no")
