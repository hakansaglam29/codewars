A = [-1,-4,7,-12]
def positive_sum(arr):
    x = 0
    for i in range(len(arr)):
        if (arr[i] > 0):
            x += arr[i]
    return x
print(positive_sum(A))

# -----2nd solution----
# def positive_sume(arr):
#     summ = 0
#     for temp in arr :
#         if temp > 0 :
#             summ += temp
#     return summ
# print(positive_sume(A))

#-------i like it------
# def positive_sume(arr):
#     return sum(i for i in arr if i < 0)
# print(positive_sume(A))