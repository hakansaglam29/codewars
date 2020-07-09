def duplicate_count(text):
    text = text.upper()
    my_dict = {i:text.count(i) for i in text}
    x = 0
    for i in my_dict.values():
        if i>1: x += 1
    return x


# def duplicate_count(text):
#     text = text.lower()
#     my_dict = {}
#     for i in text:
#         my_dict.update({i:text.count(i)})
#     x = 0
#     for i in my_dict.values():
#         if i>1: x+=1
#     return x


# Count the number of Duplicates

# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example

# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice 