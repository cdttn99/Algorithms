def dna_match_topdown(DNA1, DNA2):
    m, n = len(DNA1), len(DNA2)
    memo = [[-1 for _ in range(n)] for _ in range(m)]
    
    def lcs(i, j):
        if i == m or j == n:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if DNA1[i] == DNA2[j]:
            memo[i][j] = 1 + lcs(i + 1, j + 1)
        else:
            memo[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
        return memo[i][j]
    
    return lcs(0, 0)

def dna_match_bottomup(DNA1, DNA2):
    m, n = len(DNA1), len(DNA2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if DNA1[i - 1] == DNA2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


DNA1 = "ATAGTTCCGTCAAA"
DNA2 = "GTGTTCCGTCAAA"
print(dna_match_topdown(DNA1, DNA2))
print(dna_match_bottomup(DNA1, DNA2))

"""
Dynamic Programming paradigm
function countWaysDP(N):
    dp = array of size N+1 initialized to 0
    dp[0] = 1
    for i from 1 to N:
        if i >= 1:
            dp[i] += dp[i-1]
        if i >= 2:
            dp[i] += dp[i-2]
    return dp[N]

Brute force
function countWaysBruteForce(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return countWaysBruteForce(n-1) + countWaysBruteForce(n-2)
"""