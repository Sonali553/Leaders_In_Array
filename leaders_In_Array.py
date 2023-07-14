lst = list(map(int, input().split()))
def leaders_In_Array(lst):
    n = len(lst)
    greater_Element = lst[n - 1]
    res = [greater_Element]
    for i in range(n - 1, -1, -1):
        if lst[i] > greater_Element:
            res.append(lst[i])
            greater_Element = lst[i]
    return res
print(leaders_In_Array([16, 17, 4, 3, 5, 2]))
print(leaders_In_Array([5, 4]))
print(leaders_In_Array(lst))
