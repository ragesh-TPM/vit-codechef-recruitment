t = int(input())

for i in range(t):
    n = int(input())
    fruits = list(map(int, input().split()))
    maxfruits = 0  # for knowing the maximum fruits
    
    for start in range(n):
        basket1 = -1  # -1 is for empty basket here
        basket2 = -1
        count = 0     # initially the count will be 0
        
        for i in range(start, n):
            currentfruit = fruits[i]
            if basket1 == -1:
                basket1 = currentfruit  # using the 1st basket for any fruit that is took first.
                count += 1
            elif basket1 == currentfruit:
                count += 1     # matching the type of the fruit to check wether we can fit that on it.
            elif basket2 == -1:
                basket2 = currentfruit    # if the 2nd basket is still empty, we can use it.
                count += 1
            elif basket2 == currentfruit:
                count += 1  # if the fruit matches the 2nd basket again
            else:    # if not possible to fit in both, then as per the condition, we should stop the process
                break    
        if count > maxfruits:    # if the maximum fruit type is current one, we can change it as the maximum.
            maxfruits = count
    
    print(maxfruits)
