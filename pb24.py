
def permutations(elems):
    if len(elems)==1:
        return [elems]
    lst = []
    for e in elems:
        elems2 = elems[:]
        elems2.remove(e)
        P1 = permutations(elems2)
        P2 = [ [e]+p for p in P1]
        lst += P2
    return lst
        

print (permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[10**6-1])