def amount(A, S):
    def backtrack(start, S, path):
        if S == 0:
            result.append(list(path))
            return
        for i in range(start, len(A)):
            if i > start and A[i] == A[i-1]:
                continue  # Skip duplicates
            path.append(A[i])
            backtrack(i + 1, S - A[i], path)
            path.pop()  # Backtrack

    result = []
    backtrack(0, S, [])
    return result
print(amount([11,1,3,2,6,1,5], 8))