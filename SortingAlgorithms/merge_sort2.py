def create_array(size = 10, max = 50):
    from random import randint
    output = [randint(0,max) for _ in range(size)]
    print(output)
    return output
# Mustafa's Merge Function
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


    if (i == len(A)):
        for _ in B[j:]:
            output_list[k] = _
            # j = j + 1
            k = k + 1

    if (j == len(B)):
        for _ in A[i:]:
            output_list[k] = _
            # i = i + 1
            k = k + 1

    print(output_list)
    return output_list

# Function from tutorial
# def merge(a, b):
#     c = []
#     a_idx, b_idx = 0, 0
#     while a_idx < len(a) and b_idx < len(b):
#         if a[a_idx] < b[b_idx]:
#             c.append(a[a_idx])
#             a_idx += 1
#         else:
#             c.append(b[b_idx])
#             b_idx += 1
#
#     if a_idx == len(a): c.extend(b[b_idx:])
#     else:               c.extend(a[a_idx:])
#     return c

def merge_sort(a):
    if len(a) <= 1: return a

    mid = len(a) // 2

    left,right = merge_sort(a[:mid]), merge_sort(a[mid:])

    return merge(left, right)

a = create_array()
print(a)
s = merge_sort(a)
print(s)