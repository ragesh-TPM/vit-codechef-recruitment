t = int(input())

for i in range(t):
    word = input()
    root = word[:-2]   # to change the singular to plural just changing the last 2 letters is enough
    plural = root + "oi"
    
    print(plural)
