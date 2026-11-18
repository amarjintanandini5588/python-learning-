numbers=[2,5,2,8,5,2,9]
frequency={}
for n in numbers:
    frequency[n]=frequency.get(n,0)+1
for n in frequency:
    if frequency[n]>1:
        print(n)
