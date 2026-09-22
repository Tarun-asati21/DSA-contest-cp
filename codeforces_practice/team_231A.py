n = int(input())
total=0
for _ in range(n) :
    q1 = input().split()
    sum = 0
    for num in q1 :
        if num == "1" :
            sum+=1
    if sum >= 2 :
        total+=1
        
print(total)