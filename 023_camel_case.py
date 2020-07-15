# solution("camelCasing")  ==  "camel Casing"
s= "camelCasing"
for i in range(len(s)):
     word = ""
     for i in s:
         if i != i.capitalize():
             word += i
         else:
             word += " " + i
print(word)