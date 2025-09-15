from typing import List
from collections import deque



# def iter_board() ->:
class Solution:
    
    def coor_to_n(self, x, y) -> int:
        start_p = -len(self.board[0]) if not self.get_sense(x) else 0
        return x*len(self.board[0]) + abs(start_p + y) + 1
        
    def n_to_coor(self, n: int) -> tuple[int, int]:
        x = n//len(self.board[0])
        
        if x%2:
            y = n%len(self.board[0])
        else:
            y = len(self.board[0]) - n%len(self.board[0])

        return (x,y)
        
    def get_sense(self, row_k):
        return -1 if row_k%2 else 1

        
    def __call__(self, board: List[List[int]]) -> int:
        """
            bfs -> pick last -1 and every ladder.
            is_ladder: value > current_pos
            the first one to reach the end wins
        """
        self.board = board
        
        next_elements = deque()

        total_dice_throws = 0
        
        next_elements.append((len(board)-1, 0))

        while next_elements:
            x,y = next_elements.popleft()

            moves = 6
            total_dice_throws += 1
            for row_k in reversed(range(0, x+1)):
                sense = self.get_sense(row_k)
                col_iter = range(y, len(board[0])) if sense else range(y,0,-1)
                
                for col_k in col_iter:
                    if moves < 0:
                        break
                        
                    # if moves == 7:
                    #     moves -= 1
                    #     continue

                    if self.coor_to_n(row_k, col_k) == 1:
                        return total_dice_throws
                        
                    if board[row_k][col_k] == -1:
                        if moves == 0:
                            next_elements.append((row_k, col_k))
                    elif board[row_k][col_k] > self.coor_to_n(row_k, col_k):
                        next_elements.append((row_k, col_k))
            
                    moves -= 1

                

                    
                if moves < 0:
                    break
                
        return None
                
if __name__ == "__main__":
    s = Solution()
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

    s(board)