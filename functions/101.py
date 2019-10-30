def mult(a, b, m):
    if a * b == m:
        return True
    else: return False

def boundsCheck(l, u, length):
    if l < 0 or u > length - 1:
        return False
    else: return True

def decimalPoints(i):
    if len(i.split('.')[1]) == 3:
        return True
    else: return False

def isSorted(l):
    if l == sorted(l):
        return True
    else: return False

def reversed(l, r):
    l.reverse()
    if l == r:
        return True
    else: return False

def numOs(l):
    count = 0
    for r in l:
        for c in r:
            if c == 'o':
                count += 1
    if count == 5:
        return True
    else: return False

def printOutput(s):
    print("OUTPUT " + str(s))