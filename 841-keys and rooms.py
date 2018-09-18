
rooms = [[2], [], [3], [1, 2]]

def visitallrooms(rooms):
    # a list to store visited room
    visited = []
    stack = [] #store room that we find keys
    visited.append(0)
    stack.append(0)


    while stack:
        current_room = stack.pop()
        print("current room=", current_room)
        for i in rooms[current_room]:
            if i not in visited:
                visited.append(i)
                print("in room:", current_room, "find key:", i, "and then room visited:", visited)
                stack.append(i)
                print("rooms in stack(we are about to enter to find more keys): ", stack)

    return len(visited) == len(rooms)



print(visitallrooms(rooms))