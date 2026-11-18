numbers=[2,5,2,8,5,2,8]
frequency={}
for n in numbers:
    frequency[n]=frequency.get(n,0)+1
most_frequent=numbers[0]
highest_frequent=0
for n in frequency:
    if frequency[n]>highest_frequent:
        most_frequent=n
        highest_frequent=frequency[n]
print(most_frequent)
print(highest_frequent)
