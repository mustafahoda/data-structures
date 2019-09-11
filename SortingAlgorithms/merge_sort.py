def merge(A: list, B: list) -> list:

    output_list = [None] * (len(A) + len(B))

    i = 0
    j = 0
    k = 0

    while(i != len(A) and j != len(B)):
        if A[i] <= B[j]:
            output_list[k] = A[i]
            k = k + 1
            i = i + 1
        else:
            output_list[k] = B[j]
            k = k + 1
            j = j + 1

    print("i: %s" % i)
    print("j: %s" % j)

    if (i < len(A)):
        for _ in B[j:]:
            output_list[k] = _
            j = j + 1
            k = k + 1

    if (j < len(A)):
        for _ in A[i:]:
            output_list[k] = _
            i = i + 1
            k = k + 1

    print(output_list)
    return output_list



if __name__ == "__main__":
    merge([1,4,11,21], [2,3,5])