n = [5,2,8,1,9]

def quick_sort(n:list[int]) -> list[int]:
    if len(n) <= 1:
        return n

    pivot = n[len(n) // 2]
    left = [x for x in n if x < pivot]
    middle = [x for x in n if x == pivot]
    right = [x for x in n if x > pivot]

    return quick_sort(left) + middle + quick_sort(right) 

print (quick_sort(n))