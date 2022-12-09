# Problem statement: https://adventofcode.com/2022/day/2
options = {
    'A':1,
    'B':2,
    'C':3,
    'X':1,
    'Y':2,
    'Z':3
}



def rockPaperScissors(inputs):
    firstPlay =  options.get(inputs[0])
    secondPlay = options.get(inputs[1])
    if firstPlay > secondPlay:
        score = firstPlay + 6
        return {'winner':1, 'winner_score':score, 'loser_score':secondPlay, 'inputs':inputs, 'translated_inputs':(firstPlay, secondPlay) }
    elif firstPlay == secondPlay:
        score = firstPlay + 3
        return {'winner':0, 'winner_score':score, 'inputs':inputs, 'translated_inputs':(firstPlay, secondPlay)}
    else:
        score = secondPlay + 6
        return {'winner':2, 'winner_score':score, 'loser_score':firstPlay, 'inputs':inputs, 'translated_inputs':(firstPlay, secondPlay)}

roundScores = []
rounds = []
totalScore = 0
count = 1
with open('input', 'r') as input:
    for line in input:
        if line in ['\n', '\r\n']:
            pass
        else:
            inputs = line.strip('\n')
            inputs = inputs.split()
            rounds.append(inputs)
            result = rockPaperScissors(inputs)
            winner = result.get('winner')
            if winner == 2 or winner  == 0:
                roundScores.append(result.get('winner_score'))
                totalScore = totalScore + result.get('winner_score')
                print("Round {} score {}".format(count, result.get('winner_score')))
            else:
                roundScores.append(result.get('loser_score'))
                totalScore = totalScore + result.get('loser_score')
                print("Round {} score {}".format(count, result.get('loser_score')))
            print(result)
            print(totalScore)
            if totalScore == 10310:
                print("Round scores : {}".format(len(roundScores)))
            count = count +1
print(totalScore)
print(len(rounds))
print(len(roundScores))
if len(rounds) != len(roundScores):
    raise Exception('Rounds and rounds results don\'t match')
else:
    print(sum(roundScores))

