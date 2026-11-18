numbers=[3, 3, 7, 3, 7, 9]
frequency={}
for n in numbers:
    frequency[n]=frequency.get(n,0)+1
print(frequency)