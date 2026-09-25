def find_coin(word, char, N):
    left = 0
    right = N-1
    coin = 0
    while left <= right :
        if word[left]!=word[right]:
            if word[left] != char and word[right] != char :
                coin+=2
            else :
                coin+=1
        left+=1
        right-=1
        
    return coin

test_cases = int(input())
for _ in range(test_cases):
    lst = input().split()
    N = int(lst[0])
    char = str(lst[1])
    word = str(input())
    print(find_coin(word, char, N))
    