n=int(input("enter n:"))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit 
    n=n//10
if original==rev:
    print("it is palindrome")
else:
    print("it is not palindrome")


n1=int(str(n)[::-1])
if n==n1:
    print("it is palindrome")
else:
    print("it is not palindrome")

