# def xo(s):
#     countx = 0
#     county = 0
#     for i in s:
#         if i == "x" or i == "X":
#             countx += 1
#         if i == "o" or i == "O":
#             county += 1
#     if countx == county:
#         return True   

# def xo(s):
#     x = s.lower().count("x")
#     o = s.lower().count("o")
#     if x == o: return True 
#     else: return False

# def xo(s):
#     x = s.lower().count("x")
#     o = s.lower().count("o")
#     return x == o

def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")
