# text = 'Pig latin is cool' # igPay atinlay siay oolcay
# pig_it = 'Hello world !'     # elloHay orldway !

# pig_l= pig_it.split()
# new_pig_l = []
# for i in pig_l:
#     if len(i)!=1:
#         i = i[1:] + i[0] +"ay"
#         new_pig_l.append(i)
#     else:
#         new_pig_l.append(i)
# pig_it = " ".join(new_pig_l)



def pig_it(text):
    pig_l= text.split()
    return " ".join([i[1:]+i[0] + 'ay' if i!="?" and i!="!" else i for i in pig_l])

    


# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])