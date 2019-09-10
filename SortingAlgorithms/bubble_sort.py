def bubble_sort(A: list) -> list:

    # Base Case
    if len(A) == 1:
        return A

    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

    print(A)

if __name__ == "__main__":
    bubble_sort([3,2,1,20,5])