k,n,w = [int(num) for num in input().split()]
total_req = ((w**2 + w)*k)//2
borrow = total_req-n
if borrow > 0 :
    print(borrow)
else :
    print(0)