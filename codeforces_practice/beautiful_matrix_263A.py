
for j in range(5):
    
    lst = [int(num) for num in input().split()]

    for i,num in enumerate(lst) :
        if num == 1 :
            r, c = j+1, i+1
            
print(abs(3-r)+abs(3-c))