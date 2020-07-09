n = 7775460
# a = []
# for i in range(28):
#     while n % (i+2)==0:
#         n= n/(i+2)
#         a.append(i +2)
# k = {}
# for i in a:
#     k.update({i:a.count(i)})
# metin = ""
# for i in k:
#     if k[i] == 1:       
#         metin += "(%d)"%(i)
#     else:
#         metin += "(%d**%d)"%(i, k[i])
# print(metin)

def primeFactors(n):
    i, r = 2, ""
    while n != 1: 
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
    return r
print(primeFactors(n))