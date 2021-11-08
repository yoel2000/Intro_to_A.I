import game

DEPTH = 2


def go(gm):
    # print("In go of game ", gm.board)
    if game.isHumTurn(gm):
        # print("Turn of human")
        obj = abmin(gm, DEPTH, game.LOSS - 1, game.VICTORY + 1)[1]
        # print("object board: ",obj.board)
        return obj
    else:
        # print("Turn of agent")
        obj = abmax(gm, DEPTH, game.LOSS - 1, game.VICTORY + 1)[1]
        # print("object board: ",obj.board)
        return obj



"""
With the minimax algorith, we get the highest value that the player can be sure to get without knowing the actions of 
the other players.
"""
# s = the state (max's turn)
# d = max. depth of search
# a,b = alpha and beta
# returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmax(gm, d, a, b):
    # print("now calculate abmax")
    # print("d=",d) # the depth of the recursion (כמה צדדים רואים קדימה)
    # print("alpha=",a) # alpha and beta are representing respectively the minimum and the maximum score that the player
    # print("beta=",b)
    if d == 0 or game.isFinished(gm):
        # print("returns ", [game.value(gm), gm])
        return [game.value(gm), gm]
    v = float("-inf")
    ns = game.getNext(gm) # We save all the next situations.
    # print("next moves:", len(ns), " possible moves ")
    bestMove = 0
    for st in ns:
        tmp = abmin(st, d - 1, a, b)  # of all the ns, we see what are the best min value.
        if tmp[0] > v:
            v = tmp[0]
            bestMove = st
        if v >= b:
            return [v, st]
        if v > a:
            a = v
    return [v, bestMove]


# s = the state (min's turn)
# d = max. depth of search
# a,b = alpha and beta
# returns [v, ns]: v = state s's value. ns = the state after recomended move.
#        if s is a terminal state ns=0.
def abmin(gm, d, a, b):
    # print("now calculate abmin")
    # print("d=",d)  # for explication, see the the explication in the abmax function.
    # print("a=",a)
    # print("b=",b)

    if d == 0 or game.isFinished(gm):
        # print("returns ", [game.value(gm), gm])
        return [game.value(gm), 0]
    v = float("inf")

    ns = game.getNext(gm)
    # print("next moves:", len(ns), " possible moves ")
    bestMove = 0
    for st in ns:
        tmp = abmax(st, d - 1, a, b)  # all the 2 sides want to "maximize" their capabilities.
        if tmp[0] < v:
            v = tmp[0]
            bestMove = st
        if v <= a:
            return [v, st]
        if v < b:
            b = v
    return [v, bestMove]
