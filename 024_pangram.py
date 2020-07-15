test ="Cwm fjord bank glyphs vext quiz"
# def is_pangram(s):
#     s = s.lower()
#     for i in "abcdefghijklmnopqrstuvyxz":
#         if i not in s: return False
#     return True 

string = "abcdefghijklmnopqrstuvyxz"
def is_pangram(s):
    return set(string.lower()) <= set(s.lower())
print(is_pangram(test))