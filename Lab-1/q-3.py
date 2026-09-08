def compare_bubble_insertion(random_arr, sorted_arr, reverse_arr):
    # Optimized Bubble Sort implementation
    def bubble_sort(arr):
        arr_copy = arr[:]
        n = len(arr_copy)
        comparisons = 0
        swaps = 0
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comparisons += 1
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    swaps += 1
                    swapped = True
            if not swapped:
                break
                
        return arr_copy, comparisons, swaps

    # Insertion Sort implementation
    def insertion_sort(arr):
        arr_copy = arr[:]
        n = len(arr_copy)
        comparisons = 0
        shifts = 0
        
        for i in range(1, n):
            key = arr_copy[i]
            j = i - 1
            
            while j >= 0:
                comparisons += 1
                if arr_copy[j] > key:
                    arr_copy[j + 1] = arr_copy[j]
                    shifts += 1
                    j -= 1
                else:
                    break
            arr_copy[j + 1] = key
            
        return arr_copy, comparisons, shifts

    datasets = [
        ("Random Dataset", random_arr),
        ("Sorted Dataset", sorted_arr),
        ("Reverse Dataset", reverse_arr)
    ]

    output = ["Sorting Performance Report"]

    for dataset_name, arr in datasets:
        output.append(dataset_name)
        
        b_sorted, b_comp, b_swaps = bubble_sort(arr)
        i_sorted, i_comp, i_shifts = insertion_sort(arr)
        
        b_str = " ".join(map(str, b_sorted))
        i_str = " ".join(map(str, i_sorted))
        
        output.append(f"Bubble Sorted: {b_str}")
        output.append(f"Bubble Comparisons: {b_comp}")
        output.append(f"Bubble Swaps: {b_swaps}")
        
        output.append(f"Insertion Sorted: {i_str}")
        output.append(f"Insertion Comparisons: {i_comp}")
        output.append(f"Insertion Shifts: {i_shifts}")
        
        if b_comp < i_comp:
            output.append("Better Algorithm: Bubble Sort")
        elif i_comp < b_comp:
            output.append("Better Algorithm: Insertion Sort")
        else:
            output.append("Better Algorithm: Both Equal")

    return output