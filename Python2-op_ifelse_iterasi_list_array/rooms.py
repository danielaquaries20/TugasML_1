rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True
rooms[0][4][1] = False

print(rooms)

vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1

print(roomNumber)