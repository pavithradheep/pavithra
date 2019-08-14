def largest(arr,n): 
    max = arr[0] 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
arr = []
n = int(input())
for i in range(n):
	arr.append(int(input()))
Ans = largest(arr,n) 
print (Ans) 
