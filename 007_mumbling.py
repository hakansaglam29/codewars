def accum(s):
    b = ""
    for i in range(len(s)):
        b += (s[i]*(i+1)).capitalize() + "-"
    return b[:-1]
print(accum("hakan"))

# return "-".join(str((s[i]*(i+1)).capitalize()) for i in range(len(s)))
    
