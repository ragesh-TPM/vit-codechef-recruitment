t = int(input())

for i in range(t):
    n = int(input())
    chillies = list(map(int, input().split()))
    frequency = {}   # for knowing the spiciness for each time in form of dictionary
    
    for spice in chillies:
        if spice in frequency:
            frequency[spice] += 1
        else:
            frequency[spice] = 1
            found = False # what if the same spiciness used before comes again, so to use the data wisely we can use it as a first and last element of the list
    
    for count in frequency.values():
        if count >= 2:
            found = True
            break
    
    if not found:
        print("NO")
    else:
        print("YES")
