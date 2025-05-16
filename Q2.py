from Q1 import A,B

def mergesort(A, B):
    i = 0 #for A
    j= 0 #for B
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i]) #append stores a single value in arr at the end of list]
            i += 1
        else:
            C.append(B[j])
            j += 1
    C.extend(A[i:]) #if B runs out first,used if there are remaining elements from A, all are added at once
    C.extend(B[j:]) #if A runs out first, used if there are remaining elements from B, all are added at once
    return C

C = mergesort(A, B)
print(f"Merged array C: {C}")
assert len(C) == len(A) + len(B), "Merged array size is incorrect"
assert C == sorted(C), "Merged array is not sorted"
