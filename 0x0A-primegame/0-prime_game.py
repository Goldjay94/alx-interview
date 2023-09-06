#!/usr/bin/python3
"""0. Prime Game
"""


def isWinner(x, nums):
    """determines the winner of the game"""
    participants = {'Maria': 0, 'Ben': 0}
    if x == 0 or x is None:
        return
    for i in range(x):
        vals = [num for num in range(1, nums[i] + 1)]
        currentTurn = 'Maria'
        while vals != []:
            currentPick = vals.pop(0)
            for num in vals:
                if num % currentPick == 0:
                    vals.remove(num)
            currentTurn = 'Ben' if currentTurn == 'Maria' else 'Maria'
        participants[currentTurn] += 1
    if participants['Maria'] > participants['Ben']:
        return 'Maria'
    return 'Ben'
