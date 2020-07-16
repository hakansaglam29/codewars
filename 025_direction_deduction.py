# def dirReduc(arr):
#     for x in range(3):
#         i = 0
#         while i < len(arr)-1:
#             if arr[i]=="NORTH" and arr[i+1]=="SOUTH":
#                 arr.pop(i)
#                 arr.pop(i)
#             elif arr[i]=="SOUTH" and arr[i+1]=="NORTH":
#                 arr.pop(i)
#                 arr.pop(i)
#             elif arr[i]=="EAST" and arr[i+1]=="WEST":
#                 arr.pop(i)
#                 arr.pop(i)
#             elif arr[i]=="WEST" and arr[i+1]=="EAST":
#                 arr.pop(i)
#                 arr.pop(i)
#             else:
#                 i +=1
#     return arr

# opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
# def dirReduc(plan):
#     new_plan = []
#     for d in plan:
#         if new_plan and new_plan[-1] == opposite[d]:
#             new_plan.pop()
#         else:
#             new_plan.append(d)
#     return new_plan

def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3
plan = ["NORTH","EAST","WEST","SOUTH","WEST","WEST","NORTH"]
print(dirReduc(plan))