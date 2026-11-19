text="aabbcddee"
frequency={}
for n in text:
    frequency[n]=frequency.get(n,0)+1
for n in frequency:
    if frequency[n]==1:
        print(n)
        break

    