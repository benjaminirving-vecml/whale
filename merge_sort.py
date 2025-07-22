def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    :param arr: list of comparable elements
    :return: new sorted list
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.
    :param left: sorted list
    :param right: sorted list
    :return: merged sorted list
    """
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", sample)
    sorted_list = merge_sort(sample)
    print("Sorted:  ", sorted_list)