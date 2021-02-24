license = input()
junk = list(map(int,input().split()))
m = min(range(len(junk)), key=junk.__getitem__)
print(m)
    
