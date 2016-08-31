#Student Name: Haikun Liu                   NetID:hlg483

def binarySearch(L,v):
    """Searches through a list L for the element v using binary search method"""
    if len(L)<1: # check if there is no element in the L
        return (False,0)
    max = len(L) - 1
    min = 0
    n = 0
    while True:
        if max < min:
            return (False, n)  # no element found
        m = (min + max)//2  # using floor division here
        if L[m] < v:
            min = m + 1 # updated min value
        elif L[m] > v:
            max = m - 1 # updated max value
        else:
            return (True,n)  # element found
        n += 1


def mean(L):
    """Find the mean value of a list L"""
    if len(L) > 0:
        return float(sum(L))/len(L) # cast to float number
    else:
        return False

def median(L):
    """Find the median value of a list L"""
    if len(L) > 0:
        L = sorted(L) # using the build-in function sorted() to rearrange L
        if len(L)%2 is 1:  # odd number of elements
            return L[((len(L)+1)/2)-1]
        else:  # even number of elements
            return float(sum(L[(len(L)/2)-1:(len(L)/2)+1]))/2
    else:
        return False



def bfs(tree, elem):
    """Find the element in a tree tree using breadth first search method"""
    from collections import deque  # using deque.popleft() function
    L1 = deque(tree)
    while L1: # iterate until L1 is empty
        v = L1.popleft()  # pop the left most element v from L1
        if isinstance(v, int):  # check if v is a value
            print v
            if elem is v:  # check if elem is v
                return True
        else: # v is a list
            L2 = deque(v) # using deque.popleft() function
            while L2:
                v = L2.popleft()
                if isinstance(v, int):  # check if v is a value (optional)
                    print v
                    if elem is v:  # check if elem is v
                        return True
                else: # append the rest of element in L2 to L1
                    L1.append(v)
    return False  # no match found




def dfs(tree, elem):
    """Find the element in a tree tree using breadth first search method"""
    from collections import deque  # using deque.popleft() function
    L1 = deque(tree)
    while L1:  # iterate until L1 is empty
        v = L1.pop()  # pop the right most element v from L1
        if isinstance(v, int):  # check if v is a value
            print v
            if elem is v:  # check if elem is v
                return True
        else:  # v is a list
            L2 = deque(v)
            while L2:  # iterate until L1 is empty
                v = L2.pop()  # pop the right most element v from L2
                if isinstance(v,int):  # check if v is a value
                    L1.appendleft(v)  # append v to the LHS of L1
                else:  #  v is a list
                    v = deque(v) # using deque.appendleft() function
                    while v:  # iterate until v is empty
                        L2.appendleft(v.pop())  # append to the LHS of L1
    return False


class TTTBoard:
    def __init__(self):
        """Initialize a 3x3 tic tac toe board"""
        self.board = ['*','*','*','*','*','*','*','*','*'] # initial board pattern
        self.count = 0  # step counter, used to check if the board is full

    def __str__(self):
        """Returns a string representation of the board"""
        return str("\n" + self.board[0]) + " " + str(self.board[1]) + " " + str(self.board[2]) + "\n" + str(self.board[3]) + " " + str(self.board[4]) + " " + str(self.board[5]) + "\n" + str(self.board[6]) + " " + str(self.board[7]) + " " + str(self.board[8] + "\n")

    def makeMove(self, player, pos):
        """Places a move for player in the position pos"""
        if self.count < 9: # check if the board is full
            if self.board[pos] is '*': # check if the position is empty
                self.board[pos] = player
                self.count+=1 # increase the counter
                return True
            else:
                return False # position is occupied
        else:
            return False # the board is full

    def hasWon(self,player):
        """Returns True if player has won the game, and False if not"""

        # check horizontal
        if self.board[0] is player and self.board[1] is player and self.board[2] is player:
            return True
        elif self.board[3] is player and self.board[4] is player and self.board[5] is player:
            return True
        elif self.board[6] is player and self.board[7] is player and self.board[8] is player:
            return True

        # check vertical
        elif self.board[0] is player and self.board[3] is player and self.board[6] is player:
            return True
        elif self.board[1] is player and self.board[4] is player and self.board[7] is player:
            return True
        elif self.board[2] is player and self.board[5] is player and self.board[8] is player:
            return True

        # check diagonal
        elif self.board[0] is player and self.board[4] is player and self.board[8] is player:
            return True
        elif self.board[2] is player and self.board[4] is player and self.board[6] is player:
            return True

        else:
            return False


    def gameOver(self):
        """Returns True if someone has won or if the board is full, False otherwise"""
        if self.hasWon('X') or self.hasWon('O') or self.count >= 8: # check either X or O wins the game or the board is full
            return True
        else:
            return False

    def clear(self):
        """Clears the board to reset the game"""
        self.board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']  # initial board pattern
        self.count = 0  # step counter

