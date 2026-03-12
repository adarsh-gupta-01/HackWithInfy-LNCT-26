def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    types = set(a)
    
    ans = -1
    max_count = 0
    
    for dish in types:
        pos = []
        for i in range(n):
            if a[i] == dish:
                pos.append(i)
        
        count = 0
        prev = -2
        
        for p in pos:
            if p != prev + 1:
                count += 1
                prev = p
        
        if count > max_count:
            max_count = count
            ans = dish
        elif count == max_count:
            ans = min(ans, dish)
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()