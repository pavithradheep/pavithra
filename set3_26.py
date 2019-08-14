import statistics
n=int(input())
arr=[]
for i in range(n):
	x=int(input())
	arr.append(x)
w=arr.sort()
median=statistics.median(arr)
print(median)
