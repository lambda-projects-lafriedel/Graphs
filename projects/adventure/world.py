from room import Room
import random
import math

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {} # {Room("Room 0", "(3, 5)"", 0, 3, 5), Room("Room 1", "(3, 6)", 1, 3, 6), Room("Room 2", "(3, 7)", 2, 3, 7)}
        self.roomGrid = []
        self.gridSize = 0 # 8
    def loadGraph(self, roomGraph):
        # {0: [(3, 5), {'n': 1}], 
        # 1: [(3, 6), {'s': 0, 'n': 2}], 
        # 2: [(3, 7), {'s': 1}]}
        numRooms = len(roomGraph) # 3
        rooms = [None] * numRooms # [None, None, None]
        gridSize = 1
        for i in range(0, numRooms):
            x = roomGraph[i][0][0] # 3 // 3 // 3
            gridSize = max(gridSize, roomGraph[i][0][0], roomGraph[i][0][1])
            # gridSize = max(1, 3, 5) = 5
            # gridSoze = max(5, 3, 6) = 6
            # gridSize = max(6, 3, 7) = 7
            self.rooms[i] = Room(f"Room {i}", f"({roomGraph[i][0][0]},{roomGraph[i][0][1]})",i, roomGraph[i][0][0], roomGraph[i][0][1])
            # self.rooms[0] = Room("Room 0", "(3, 5)"", 0, 3, 5)
            # self.rooms[1] = Room("Room 1", "(3, 6)", 1, 3, 6)
            # self.rooms[2] = Room("Room 2", "(3, 7)", 2, 3, 7)
            # Room(name, description, id, x, y)
        self.roomGrid = []
        gridSize += 1
        # gridSize = 8
        self.gridSize = gridSize
        for i in range(0, gridSize):
            self.roomGrid.append([None] * gridSize)
            # self.roomGrod = [None, None, None, None, None, None, None, None]
        # for key of room graph
        for roomID in roomGraph:
            room = self.rooms[roomID]
            # room = Room("Room 0", "(3, 5)"", 0, 3, 5)
            self.roomGrid[room.x][room.y] = room
            # self.roomGrid[3][5] = Room("Room 0", "(3, 5)"", 0, 3, 5)
            if 'n' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('n', self.rooms[roomGraph[roomID][1]['n']])
            if 's' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('s', self.rooms[roomGraph[roomID][1]['s']])
            if 'e' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('e', self.rooms[roomGraph[roomID][1]['e']])
            if 'w' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('w', self.rooms[roomGraph[roomID][1]['w']])
        self.startingRoom = self.rooms[0]

    def printRooms(self):
        rotatedRoomGrid = []
        for i in range(0, len(self.roomGrid)):
            rotatedRoomGrid.append([None] * len(self.roomGrid))
        for i in range(len(self.roomGrid)):
            for j in range(len(self.roomGrid[0])):
                rotatedRoomGrid[len(self.roomGrid[0]) - j - 1][i] = self.roomGrid[i][j]
        print("#####")
        str = ""
        for row in rotatedRoomGrid:
            allNull = True
            for room in row:
                if room is not None:
                    allNull = False
                    break
            if allNull:
                continue
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        print(str)
        print("#####")


