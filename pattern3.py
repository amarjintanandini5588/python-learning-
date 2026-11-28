n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(i):
        sum=1
        sum=sum+j
        print(sum,end=" ")
    print()