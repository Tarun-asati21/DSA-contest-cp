word = str(input())
lst = []
for ch in word :
    if ch!="+" :
        lst.append(int(ch))
lst.sort()
for i,num in enumerate(lst) :
    if i == len(lst)-1 :
        print(str(num))
    else :
        print(str(num)+"+", end="")