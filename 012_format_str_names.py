# names = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

def namelist(names):
    length = len(names)
    alist = []
    a = -1
    name = ""
    for i in names:
        alist.append(list(i.values()))
        a += 1
        if a != (length-2):
            name += alist[a][0] + ", "
        else:
            name += alist[a][0] + " & "
    return name[:-2]

# # def namelist(names):
# #     if len(names) > 1:
# #         return '{} & {}'.format(' - '.join(name['name'] for name in names[:-1]), 
# #                                 names[-1]['name'])
# #     elif names:
# #         return names[0]['name']
# #     else:
# #         return ''