s = 'i want to travel the world writing code one day'
def find_short(s):
    l = s.split()
    return len(min(l, key=len))

print(find_short(s))

# Shortest Word
# Simple, given a string of words, 
# return the length of the shortest word(s).
# String will never be empty and you do not need 
# to account for different data types.

# string.split(s[, sep[, maxsplit]])
# Return a list of the words of the string s. If the optional second argument sep is absent or None, 
# the words are separated by arbitrary strings of whitespace characters (space, tab, newline, return, formfeed). 
# If the second argument sep is present and not None, it specifies a string to be used as the word separator. 
# The returned list will then have one more item than the number of non-overlapping occurrences 
# of the separator in the string. If maxsplit is given, at most maxsplit number of splits occur, 
# and the remainder of the string is returned as the final element of the list (thus, the list will 
# have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit 
# on the number of splits (all possible splits are made).

# The behavior of split on an empty string depends on the value of sep. 
# If sep is not specified, or specified as None, the result will be an empty list.
# If sep is specified as any string, the result will be a list containing one element which is an empty string.