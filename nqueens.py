'''
def isSafe(i, j, board):
  for c in range(len(board)):
    for r in range(len(board)):
      # check if i,j share row with any queen
      if board[c][r] == 'q' and i==c and j!=r: 
        return False
      # check if i,j share column with any queen
      elif board[c][r] == 'q' and j==r and i!=c:
        return False
      # check if i,j share diagonal with any queen
      elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
        return False
  return True 

def nQueens(r, n, board):
  # base case, when queens have been placed in all rows return
  if r == n:
    return True, board
  # else in r-th row, check for every box whether it is suitable to place queen
  for i in range(n):
    if isSafe(r, i, board):
      # if i-th columns is safe to place queen, place the queen there and check recursively for other rows
      board[r][i] = 'q'
      okay, newboard = nQueens(r+1, n, board)
      # if all next queens were placed correctly, recursive call should return true, and we should return true here too
      if okay:
        return True, newboard
      # else this is not a suitable box to place queen, and we should check for next box
      board[r][i] = '-'
  return False, board

def placeNQueens(n, board):

  
  return nQueens(0, n, board)[1]

def main():
  n = 4
  board = [["-" for _ in range(n)] for _ in range(n)]
  qBoard = placeNQueens(n, board)
  qBoard =  "\n".join(["".join(x) for x in qBoard])
  print (qBoard)
main()
'''

#//////////////////////////////////////////////////////////////////////////////////////////////

finalSol = []

def act(indx, indy, cols, rows, ops, opr, tmpSol):
    nOps = list(ops)
    nOpr = list(opr)
    nTmpSol = list(tmpSol)
    nCols = list(cols)
    nRows = list(rows)
    nOps.append(cols[indx] + rows[indy])
    nOpr.append(cols[indx] - rows[indy])
    nTmpSol.append((cols[indx], rows[indy]))
    del nCols[indx]
    del nRows[indy]
    return nCols, nRows, nOps, nOpr, nTmpSol

def verif(x, y, ops, opr):
    if (x + y in ops) or (x - y in opr):
        return False
    return True

def posNQ(cols, rows, ops = [], opr = [], tmpSol = []):
    lim = len(cols)
    if lim == 1:
        if verif(cols[0], rows[0], ops, opr):
            tmpSol.append((cols[0], rows[0]))
            tmpSol.sort()
            if tmpSol not in finalSol:
                #print('\n\nSolución: ', tmpSol)
                finalSol.append(tmpSol)
            del cols, rows, ops, opr, tmpSol
        else:
            #print('No solution')
            del cols, rows, ops, opr, tmpSol
    else:
        if len(finalSol) != 1:
            for i in range(lim):
                for j in range(lim):
                    if verif(cols[i], rows[j], ops, opr):
                        nCols, nRows, nOps, nOpr, nTmpSol = act(i, j, cols, rows, ops, opr, tmpSol)
                        posNQ(nCols, nRows, nOps, nOpr, nTmpSol)

def placeNQueens(n, board):
    cols = []
    rows = []
    for i in range(n):
        cols.append(i+1)
        rows.append(i+1)
    posNQ(cols, rows)
    #print(finalSol)
    row = []
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            if ((finalSol[0][i][0] - 1) == i) and ((finalSol[0][i][1] - 1) == j):
                row.append('q')
            else:
                row.append('-')
        board.append(row)
            
    return board

if __name__ == '__main__':
    n = 5
    b = []
    cad = ['-' for _ in range(n)]
    for i in range(n):
        b.append(''.join(cad))
    test = placeNQueens(n, b)
    print(test)