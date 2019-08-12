net=int(input())
ket=int(input())
for num in range (net+1,ket):
	if num>1:
		for n in range(2,num):
			if(num%n)==0:
				break
		else:
			print(num)
