n, k = [int(num) for num in (input().split())]
scores = [int(num) for num in (input().split())]
kth_score = scores[k-1]

low = 0
high = n-1
lb = -1

while low <= high :
    mid = low + (high-low)//2
    if scores[mid] >= kth_score and scores[mid]>0 :
        lb = mid
        low = mid+1
    else :
        high = mid-1

print(lb+1)