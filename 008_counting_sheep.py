# def count_sheeps(sheep):
#     a = 0
#     for i in sheep:
#         if i == True:
#             a += 1
#     return a

# def count_sheeps(sheep):
#     return len([i for i in sheep if i == True])

def count_sheeps(x):
    return x.count(True)

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]
  
print(count_sheeps(array1))