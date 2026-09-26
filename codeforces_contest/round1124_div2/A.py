def helper (N, K):
    return 2**(N-K+1) + 2*(K-1)

testcases = int(input())
for _ in range(testcases):
    N, K = [int(num) for num in input().split()]
    print(helper(N,K))