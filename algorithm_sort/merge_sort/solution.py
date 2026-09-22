n = [5,2,8,1]

def merge_sort(n:int) -> list[int]:
    s = len(n)
    for i in range(s):
        for j in range(0, s-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

print(merge_sort(n))

