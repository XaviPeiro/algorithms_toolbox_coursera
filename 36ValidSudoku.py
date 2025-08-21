from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        create_cols + create_rooms = n + n = O(n)
        [check_repeated = n = O(n)]
        check_line + check_cols + check_rooms = n + n + n = 3n = O(n)
        ---
        Total = 5n = O(n)
        
        """
        def check_repeated(board: List[List[str]]) -> bool:
            empty_cell = "."
            for line in board:
                track = {}
                for el in line:
                    if el == empty_cell:
                        continue
                    g = track.get(el, None)

                    if g is not None:
                        print(track)
                        print(line)
                        print(f"{g} - {el}")
                        return False
                    else:
                        track[el] = 1
            return True

        # lines
        lines_check = check_repeated(board)
        if lines_check is False:
            print("lines failed!")
            return False
        
        # Transform data
        columns = []
        rooms = []
        lenline = 3
        for rowi, rowv in enumerate(board):
            for coli, colv in enumerate(rowv):
                # columns
                try:
                    columns[coli].append(colv)
                except IndexError:
                    columns.append([])
                    columns[coli].append(colv)
                
                # roms
                try:
                    roomi = (coli//3) + lenline*(rowi//3)
                    rooms[roomi].append(colv)
                except IndexError:
                    rooms.append([])
                    print(f"roooomi: {roomi}")
                    rooms[roomi].append(colv)
        # columns
        columns_check = check_repeated(columns)
        if columns_check is False:
            print("cols failed!")

            return False
        # rooms
        print(rooms)

        rooms_check = check_repeated(rooms)
        if rooms_check is False:
            print("rooms failed!")
            return False

        return True


                    

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols_dict = set()
        empty_char = "."
        rooms_dict = defaultdict()
        for rowi, row in enumerate(board):
            
            row_dict = set()
            for coli, val in enumerate(row):
                if val == empty_char:
                    continue

                # check cols
                col_vals = cols_dict.get(coli)
                if col_vals is None:
                    cols_dict[coli] = {}
                    col_vals = cols_dict.get(coli)
                
                vincol = col_vals.get(val)
                if vincol is not None:
                    return False
                else:
                    col_vals[vincol] = 1
                
                # check rows
                vinrow = row_dict.get(val, None)
                if vinrow is not None:
                    return False
                else:
                    row_dict[val] = 1

                # check room
                krooms = f"{coli//3}{rowi//3}"
                room_vals: dict = rooms_dict[krooms]
                vinrooms = rooms_vals.get(val)
                if vinrooms is None:
                    room_vals[val] = 1
                else:
                    return False
        return True