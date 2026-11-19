numbers=[4,7,2,9,9]
seen=set()
for n in numbers:
    if n in seen:
        print(n)
        break
    else:
        seen.add(n)