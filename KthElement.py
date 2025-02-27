"""function kthElement(Arr1, Arr2, k):
    # Base cases
    if length of Arr1 is 0:
        return Arr2[k-1]
    if length of Arr2 is 0:
        return Arr1[k-1]
    if k == 1:
        return min(Arr1[0], Arr2[0])

    # Calculate the mid points
    mid1 = min(k//2, length of Arr1) - 1
    mid2 = min(k//2, length of Arr2) - 1

    if Arr1[mid1] <= Arr2[mid2]:
        return kthElement(Arr1[mid1 + 1:], Arr2, k - (mid1 + 1))
    else:
        return kthElement(Arr1, Arr2[mid2 + 1:], k - (mid2 + 1))
"""
def kthElement(Arr1, Arr2, k):
    # Base cases
    if len(Arr1) == 0:
        return Arr2[k-1]
    if len(Arr2) == 0:
        return Arr1[k-1]
    if k == 1:
        return min(Arr1[0], Arr2[0])

    # Calculate the mid points
    mid1 = min(k // 2, len(Arr1)) - 1
    mid2 = min(k // 2, len(Arr2)) - 1

    if Arr1[mid1] <= Arr2[mid2]:
        return kthElement(Arr1[mid1 + 1:], Arr2, k - (mid1 + 1))
    else:
        return kthElement(Arr1, Arr2[mid2 + 1:], k - (mid2 + 1))

Arr1 = [1, 2, 3, 5, 6]
Arr2 = [3, 4, 5, 6, 7]
k = 5
print(kthElement(Arr1, Arr2, k)) 
