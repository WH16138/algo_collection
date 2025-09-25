pivot_seq = []

def quick_sort(arr):
    global pivot_seq

    if len(arr) <= 1:
        return arr
    
    L, R = 0, len(arr)-1
    M = (L+R)//2 
    temp = [(L, arr[L]), (M, arr[M]), (R, arr[R])]
    for i in range(3):
        for j in range(i+1, 3):
            if temp[i][1] > temp[j][1]:
                temp[i], temp[j] = temp[j], temp[i]
    pivot = temp[1][0]
    arr[L], arr[pivot] = arr[pivot], arr[L]
    pivot = L
    pivot_seq.append(arr[pivot])
    while L <= R:
        while arr[L] < arr[pivot]:
            L += 1
        while arr[R] > arr[pivot]:
            R -= 1
        if L <= R:
            arr[L], arr[R] = arr[R], arr[L]
            L += 1
            R -= 1
    arr[L] , arr[R] = arr[R], arr[L]
    print(L,R)
    
    left = quick_sort(arr[1:R-1])
    right = quick_sort(arr[L:])
    return left + [arr[pivot]] + right

N = int(input())
arr = list(map(int, input().split()))
ans = quick_sort(arr)
print('_'.join(map(str, pivot_seq)))
print('_'.join(map(str, ans)))