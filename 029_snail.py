array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a

print(snail(array))

# def snail(array):
#     dizi= []
#     n = len(array)
#     while n>0:
#         if array==[[]]: break
#         for i in range(len(array)-1):
#             if i == 0:
#                 dizi.extend(array[i])
#                 array.pop(i)
#                 n -= 1
#                 dizi.append(array[i][-1])
#             else:
#                 dizi.append(array[i][-1])
#         for i in range(len(array)-1,-1,-1):
#             dizi.append(array[-1][i])
#         array.pop(-1)
#         n -= 1
#         for i in range(len(array)-1,-1,-1):
#             dizi.append(array[i][0])
#         array2=[]
#         for i in array:
#             array2.append(i[1:-1])
#         array = array2
#     return dizi