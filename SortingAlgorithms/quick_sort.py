from random import randint

def quicksort(a):
    if len(a) <= 1: return a

    smaller, equal, larger = [], [], []
    pivot = a[randint(0, len(a) - 1)]

    for x in a:
        if x<pivot:             smaller.append(x)
        elif x == pivot:        equal.append(x)
        else:                   larger.append(x)

    return quicksort(smaller) + equal + quicksort(larger)


def create_array(size = 10, max = 50):
    return [randint(0, max) for _ in range(size)]

if __name__ == "__main__":
    # print(quick_sort([2,1,3]))
    a = create_array()
    print("a: %s" % a)
    s = quicksort(a)
    print(s)