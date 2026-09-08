def compare_search_algorithms(arr, target):
    # 1. Linear Search (Unconditional full scan until match or end)
    linear_idx = -1
    linear_count = 0
    
    for i in range(len(arr)):
        linear_count += 1
        if arr[i] == target:
            linear_idx = i
            break

    # 2. Binary Search (First Occurrence)
    binary_idx = -1
    binary_count = 0
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        binary_count += 1
        
        if arr[mid] == target:
            binary_idx = mid
            right = mid - 1  # Continue searching left side for first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # 3. Determine Better Algorithm
    if binary_count < linear_count:
        better_algo = "Better Algorithm: Binary Search"
    elif linear_count < binary_count:
        better_algo = "Better Algorithm: Linear Search"
    else:
        better_algo = "Better Algorithm: Both Equal"

    return [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {linear_idx}",
        f"Comparisons: {linear_count}",
        "Binary Search",
        f"Index: {binary_idx}",
        f"Comparisons: {binary_count}",
        better_algo
    ]