n = [5,2,8,1]

def selection_sort(n:list[int]) -> list[int]:
    s = len(n)
    for i in range(s): 
        min_value = i 
        for j in range(i+1, s):
            if n[j] < n[min_value]:
                min_value = j
                n[j], n[min_value] = n[min_value], n[j]

    return n

print(selection_sort(n))



