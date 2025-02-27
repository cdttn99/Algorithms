def powerset(inputSet):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(inputSet)):
            path.append(inputSet[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

print(powerset([1, 2, 3]))
print(powerset([]))