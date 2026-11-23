n=int(input("enter n:"))
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
        break
if prime:
    print(n,"is prime")
else:
    print(n,"is not prime")