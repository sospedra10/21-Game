def who(winner):
    if winner == 'ia':
        return 'Ia wins'
    elif winner == 'user':
        return 'User wins'
    else:
        return 'err'

def nextTurn(now):
    if now == 'ia':
        return 'user'
    return 'ia'

def isWinner(n, turn):
    winner = ' '

    if n >= 21:
        if turn == 'ia':
            return 'user'
        else:
            return 'ia'
    return winner

def playUser(n):
    print()
    print("User +", end = ' ')
    new = int(input())
    while new < 1 or new > 3:
        print("User's turn: ", end = ' ')
        new = int(input())
    print(n + new)
    return n + new

def playIa(n, turn):
    print("Ia +", end = ' ')
    bestScore = float("-inf")
    bestMove = 1
    
    for i in range(1, 4):
        score = minimax(turn, n + i, 0, False)
        if score > bestScore:
            bestScore = score
            bestMove = i
    print(bestMove)
    print(n + bestMove)
    return n + bestMove

def minimax(turn, new, depth, isMaximizing):
    result = isWinner(new, turn)
    if result != ' ':
        return scores[result] 


    if isMaximizing:
        bestScore = float("-inf")
        new_turn = nextTurn(turn)
        for i in range(1, 4):
            score = minimax(new_turn, new + i, depth + 1, False)
            bestScore = max(score, bestScore)
        return bestScore - depth 
    else:
        bestScore = float("inf")
        new_turn = nextTurn(turn)
        for i in range(1, 4):
            score = minimax(new_turn, new + i, depth + 1, True)
            bestScore = min(score, bestScore)
        return bestScore



scores = {
    'ia': 10,
    'user': -10,
}

winner = ' '
turn = 'user'
n = 0

while winner == ' ':
    if turn == 'ia':
        n = playIa(n, turn)
    else:   
        n = playUser(n)
        
    winner = isWinner(n, turn)
    turn = nextTurn(turn)


print(who(winner))