def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    index = -1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index, comparisons


# Test data
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

linear_index, linear_comp = linear_search(arr, target)
binary_index, binary_comp = binary_search(arr, target)

print("Search Comparison Report")
print("Linear Search")
print("Index:", linear_index)
print("Comparisons:", linear_comp)
print("Binary Search")
print("Index:", binary_index)
print("Comparisons:", binary_comp)

if linear_comp < binary_comp:
    print("Better Algorithm: Linear Search")
elif binary_comp < linear_comp:
    print("Better Algorithm: Binary Search")
else:
    print("Better Algorithm: Both Equal")