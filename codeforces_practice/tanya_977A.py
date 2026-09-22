n,k = [int(num) for num in input().split()]

number = n
for _ in range(k) :
    if str(number)[-1] == "0" :
        number = number//10
    else :
        number -= 1

print(number)