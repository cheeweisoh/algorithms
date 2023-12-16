import collections

class Solution:
    def get_index(self, pos: int, n: int) -> list:
        """Get Index From Position

        Args:
            pos (int): position on board
            n (int): size of board

        Returns:
            coords (list): indexes of position on boustrophedon style board
        """
        r = n - ((pos-1) // n) - 1
        if n%2:
            c = n - ((pos-1) % n) - 1 if r%2 else (pos-1) % n
        else:
            c = (pos-1) % n if r%2 else n - ((pos-1) % n) - 1 
        
        coords = [r,c]
        return coords
    
    def snakesAndLadders(self, board: list) -> int:
        """Snakes and Ladders

        Args:
            board (list): boustrophedon style snakes and ladders board where destination of snake or ladder on (r, c) is board[r][c], -1 if there is no snake or ladder

        Returns:
            ans (int): least number of moves required to reach n^2, -1 if not possible
        """
        n = len(board)
        visited = [0] * n**2
        ans = n**2 + 1
        
        q = collections.deque()
        q.append([1,0])
        
        while q:
            curr_pos, moves = q.popleft()
            
            for i in range(1, 7):
                new_pos = curr_pos + i
                r, c = self.get_index(new_pos, n)
                if board[r][c] != -1:
                    new_pos = board[r][c]
                
                if new_pos >= n**2:
                    ans = min(ans, moves+1)
                    break
                
                if not visited[new_pos-1]:
                    q.append([new_pos, moves+1])
                    visited[new_pos-1] = 1
                    
        return ans if ans != n**2 + 1 else -1