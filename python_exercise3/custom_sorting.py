def bubble_sort(numbers):
    n = len(numbers)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
def bubble_sort_descending(numbers):
    n = len(numbers)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is less than the next element
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numbers)
print("Sorted (Ascending):", bubble_sort(numbers))
print("Sorted (Descending):", bubble_sort_descending(numbers))