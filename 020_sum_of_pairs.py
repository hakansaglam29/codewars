l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

# Sum of Pairs
# Given a list of integers and a single sum value, 
# return the first two values (parse from the left please) 
# in order of appearance that add up to form the sum.
a = 0
s = 8
for i in l1:
    print(i)
    l1.remove(i)
    for k in l1:
        print(k)
