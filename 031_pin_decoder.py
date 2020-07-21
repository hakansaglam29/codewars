from itertools import product # Bu modül elemanlari kartezyen sekilde bir araya getiriyor.

def get_pins(observed):
    decoder= [("0","8"),("1","2","4"),["2","1","3","5"],("3","2","6"),\
              ("4","7","1","5"),("5","2","4","6","8"),("6","3","5","9"),\
              ("7","8","4"),("8","7","5","9","0"),("9","6","8")]
    dol = [decoder[int(i)]for i in observed]
    k = list(product(*dol))
    return ["".join(a) for a in k]


# adjacents = {
#   '1': ['2', '4'],
#   '2': ['1', '5', '3'],
#   '3': ['2', '6'],
#   '4': ['1', '5', '7'],
#   '5': ['2', '4', '6', '8'],
#   '6': ['3', '5', '9'],
#   '7': ['4', '8'],
#   '8': ['5', '7', '9', '0'],
#   '9': ['6', '8'],
#   '0': ['8'],
# }

# def get_pins(observed):
#   if len(observed) == 1:
#     return adjacents[observed] + [observed]
#   return [a + b for a in adjacents[observed[0]] + [observed[0]] for b in get_pins(observed[1:])]




# from itertools import product

# ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

# def get_pins(observed):
#     return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]


# from itertools import product

# PIN = {'1': ('1', '2', '4'), 
#        '2': ('1', '2', '3', '5'), 
#        '3': ('2', '3', '6'), 
#        '4': ('1', '4', '5', '7'), 
#        '5': ('2', '4', '5', '6', '8'), 
#        '6': ('5', '6', '9', '3'), 
#        '7': ('4', '7', '8'), 
#        '8': ('7', '5', '8', '9', '0'), 
#        '9': ('6', '8', '9'), '0': ('0', '8')}

# observed = "12"
# def get_pins(observed):
#     return [''.join(a) for a in product(*(PIN[i] for i in observed))]
