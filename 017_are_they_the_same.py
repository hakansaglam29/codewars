a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
def comp(array1, array2):
    if array1 == None or array2 == None: return False
    a1_new = []
    for i in array1:
        a1_new.append(i**2)
    a1_new.sort()
    array2.sort()
    if a1_new == array2: return True
    else: return False
print(comp(a1,a2))

# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False

# Given two arrays a and b write a function comp(a, b)
# that checks whether the two arrays have the "same" elements,
# with the same multiplicities. "Same" means, here,
# that the elements in b are the elements in a squared,
# regardless of the order.