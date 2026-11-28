n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(n+1-i):
        print(" ",end=" ")
    for k in range(2*i-n):
        print("*",end=" ")
    print() 
