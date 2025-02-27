def max_independent_set(nums):
    if not nums:
        return []
    
    n = len(nums)
    if n == 1:
        return [nums[0]] if nums[0] > 0 else []
    
    dp = [0] * n
    if nums[0] > 0:
        dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    result = []
    i = n - 1
    while i >= 0:
        if i == 0:
            if dp[i] > 0:
                result.append(nums[i])
            break
        if dp[i] != dp[i-1]:
            result.append(nums[i])
            i -= 2
        else:
            i -= 1
    
    return result[::-1]

print(max_independent_set([7, 2, 5, 8, 6]))