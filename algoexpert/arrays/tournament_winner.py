"""https://www.algoexpert.io/questions/tournament-winner"""

def tournamentWinner(competitions, results):
    scores = {}

    for i in range(len(competitions)):
        if results[i] == 0:
            scores[competitions[i][1]] = 3 + scores.get(competitions[i][1], 0)
        else:
            scores[competitions[i][0]] = 3 + scores.get(competitions[i][0], 0)

    sk = list(scores.keys())
    m = sk[0]

    for i in range(1, len(scores)):
        if scores[m] < scores[sk[i]]:
            m = sk[i]

    return m
