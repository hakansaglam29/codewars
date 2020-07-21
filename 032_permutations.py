# daily-python-challenge
# Define a “function” to calculate permutation of 2 numbers.
# Reminder: P(n,r) = n!/(n-r)!
# Clue: Defining a function that calculates factorial of given number, may be helpful.

from itertools import permutations
def P(n,r):
    return len(list(permutations(range(n),r)))