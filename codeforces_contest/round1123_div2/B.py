from collections import Counter
 
def process_test_case(arr):
 
    freq = Counter(arr)
    keys = sorted(freq.keys(), reverse=True)
    
    ans = []
    
    # Run the logic until all frequencies are 0
    while any(freq[k] > 0 for k in keys):
        # Find the largest key that still has remaining frequency
        top_key = None
        for k in keys:
            if freq[k] > 0:
                top_key = k
                break
        
        c = freq[top_key]
        ans.extend([top_key] * c)
        freq[top_key] = 0
        
        # Match smaller keys against the count 'c'
        for k in keys:
            if k < top_key and freq[k] > 0:
                to_add = min(freq[k], c)
                ans.extend([k] * to_add)
                freq[k] -= to_add
 
    return ans
 
# Read line by line
t = int(input().strip())
 
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    # Pass the array line by line into the function
    result = process_test_case(arr)
    
    # Output space-separated array
    print(*result)