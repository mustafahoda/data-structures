def selection_sort(A: list) -> list:

    if len(A) == 1:
        print(A)
        return A

    sorted_ptr = 0
    while sorted_ptr != len(A) - 1:

        min = A[sorted_ptr]

        for _ in range(sorted_ptr + 1, len(A)):
            if A[_] < min:
                min = A[_]
                min_index = _

        # Swap it!
        temp = A[sorted_ptr]
        A[min_index] = temp
        A[sorted_ptr] = min

        sorted_ptr += 1


    print(A)
    return A



if __name__ == "__main__":
    selection_sort([10])