def find_nb(m):
    x = sum = 0
    while sum < m: x += 1; sum += x**3
    if sum == m: return x
    elif sum > m: return -1

# print(find_nb(4183059834009))