arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # should be 6: [4, -1, 2, 1]


# def maxSequence(arr):
#     return max([sum(arr[i:j]) for i in range(len(arr)+1) for j in range(len(arr)+1)])
# print(maxSequence(arr))

def maxSequence(arr):
    summ=[]
    for j in range(len(arr)+1):
        for i in range(len(arr)+1):
            summ.append(sum(arr[i:j]))
    return max(summ)
print(maxSequence(arr))