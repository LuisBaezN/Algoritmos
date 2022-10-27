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
        for i in range(lim):
            for j in range(lim):
                if verif(cols[i], rows[j], ops, opr):
                    nCols, nRows, nOps, nOpr, nTmpSol = act(i, j, cols, rows, ops, opr, tmpSol)
                    posNQ(nCols, nRows, nOps, nOpr, nTmpSol)

if __name__ == '__main__':
    cols = []
    rows = []
    for i in range(10):
        cols.append(i+1)
        rows.append(i+1)
    posNQ(cols, rows)
    print('Número de soluciones: ', len(finalSol), '\nPosiciones: ', finalSol)