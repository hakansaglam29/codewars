def valid_parentheses(string):
    string= "".join([i for i in string if i=="(" or i==")"])
    for i in range(len(string)//2):
        string = string.replace("()",'') 
    return False if string !="" else True 

# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False