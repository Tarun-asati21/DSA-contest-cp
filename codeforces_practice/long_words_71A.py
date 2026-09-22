n = int(input())
words =[]
for _ in range(n) :
    word = str(input())
    words.append(word)

def helper(word) :
    if len(word) <= 10 :
        print(word)
    else :
        print(word[0] + str(len(word[1:-1])) + word[-1])

for word in words :
    helper(word)