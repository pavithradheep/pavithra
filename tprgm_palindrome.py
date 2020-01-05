n=int(input())
rev=0
temp=n
while(n>0):
    dig=n%10	
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("no. is palindrome")
else:
    print("no. is not palindrome")

