def bubbleSort(A):
    swap = True
    n = len(A)-1
    while n > 0 and swap:
        swap = False
        for i in range(n):
            if A[i] > A[i+1]:
                swap = True
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
        n -= 1

l = [21,4,1,3,9,20,25,6,21,14]
bubbleSort(l)
print(l)