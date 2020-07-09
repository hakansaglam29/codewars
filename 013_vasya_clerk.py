def tickets(people):
    d25 = d50 = d100 = 0
    for i in people:
        if i == 25      : d25+=1
        elif i == 50:
            if d25 >= 1 : d50+=1; d25-=1
            else: return "NO"
        else:
            if d50 >=1 and d25>=1: d100+=1; d50-=1; d25-=1
            elif d25>=3: d100+=1; d25-=3
            else: return "NO"
    return "YES"

people = [25, 25, 25, 25, 25, 50, 100]
print(tickets(people))
