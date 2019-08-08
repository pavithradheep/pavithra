num=int(input())
if(num>1):
	for i in range(2,n):
		if((num%i)==0):
			print("no")
			break
	else:
		print("yes")
else:
	print("no")
