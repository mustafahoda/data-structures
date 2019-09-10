def insertion_sort(A: list) -> list:

    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j+1] and j >= 0:
            print("i: %s" % i)
            print("j: %s" % j)
            print([A])
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1

    print(A)


if __name__ == "__main__":
    insertion_sort([7,8,5,4,9,7])