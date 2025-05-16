import random

A = [random.randint(0,1024) for _ in range(256)]
B = [random.randint(0,1024) for _ in range(300)]


#shellsort on A
def shellsort(arr):
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j-gap
            arr[j] = temp

        gap = gap // 2
    return arr

#quicksort on B
def quicksort(arr):
    def partition(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high

        while True:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] >= pivot:
                right -= 1
            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]
        return right

    def quicksort_helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort_helper(arr, low, pivot_index - 1)
            quicksort_helper(arr, pivot_index + 1, high)

    quicksort_helper(arr, 0, len(arr) - 1)
    return arr

A = shellsort(A)
B = quicksort(B)

if __name__ =="__main__":
    print(f"Sorted array A:",A)
    print(f"Sorted array B:",B)

assert shellsort(A) == sorted(A), "Shell Sort failed"
assert quicksort(B) == sorted(B), "Quick Sort failed"





