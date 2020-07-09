# def number(bus_stops):
#     num_people = 0
#     for i in bus_stops:
#         num_people += i[0]
#         num_people -= i[1]
#     return num_people

# def number(stops):
#     return sum(i - o for i, o in stops)

def number(bus_stops):
    return sum(i[0]-i[1] for i in bus_stops)

bus = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
print(number(bus))