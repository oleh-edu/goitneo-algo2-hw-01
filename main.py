#!/usr/bin/env python

def find_min_max(array):
    def divide_and_conquer(arr, left, right):
        print(f"[*] divide_and_conquer called with left={left}, right={right}")
        # Basic case: if the array has only one element
        if left == right:
            print(f"[*] Single element case: {arr[left]}")
            return arr[left], arr[left]

        # If the array has two elements
        if right == left + 1:
            print(f"[*] Two elements case: {arr[left]} and {arr[right]}")
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]

        # Divide the array into two parts
        mid = (left + right) // 2
        print(f"[*] Dividing: left={left}, mid={mid}, right={right}")
        left_min, left_max = divide_and_conquer(arr, left, mid)
        print(f"[*] Results from left part: min={left_min}, max={left_max}")
        right_min, right_max = divide_and_conquer(arr, mid + 1, right)
        print(f"[*] Results from right part: min={right_min}, max={right_max}")

        # Combining the results
        overall_min = min(left_min, right_min)
        overall_max = max(left_max, right_max)
        print(f"[*] Combined results: overall_min={overall_min}, overall_max={overall_max}")

        return overall_min, overall_max

    # Calling a recursive function for the entire array
    if not array:
        raise ValueError("The array cannot be empty")

    print(f"[*] Starting find_min_max with array={array}")
    result = divide_and_conquer(array, 0, len(array) - 1)
    return result

# Example of use
if __name__ == "__main__":
    array = [5, 1, 7, 4, 5, 15, 4, 1, 25, 3, 8, 5]
    result = find_min_max(array)
    print(f"[*] Final result: min={result[0]}, max={result[1]}")
