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
    firstPlayWeight =  options.get(inputs[0])
    secondPlayWeight = options.get(inputs[1])

    if firstPlayWeight == secondPlayWeight:
        score = firstPlayWeight + 3
        return {'winner':0, 'winner_score':score, 'inputs':inputs, 'translated_inputs':(firstPlayWeight, secondPlayWeight)}
    if firstPlayWeight == 1 and secondPlayWeight != 2:
            return {'winner':1, 'winner_score':7, 'loser_score':secondPlayWeight, 'inputs':inputs, 'translated_inputs':(firstPlayWeight, secondPlayWeight) }
    if secondPlayWeight == 1 and firstPlayWeight != 2:
            return {'winner':2, 'winner_score':7, 'loser_score':firstPlayWeight, 'inputs':inputs, 'translated_inputs':(firstPlayWeight, secondPlayWeight) }
    if firstPlayWeight > secondPlayWeight:
            score = firstPlayWeight + 0
            return  {'winner':1, 'winner_score':score, 'loser_score':secondPlayWeight, 'inputs':inputs, 'translated_inputs':(firstPlayWeight, secondPlayWeight) }
    else:
        score = secondPlayWeight + 6
        return {'winner':2, 'winner_score':score, 'loser_score':firstPlayWeight, 'inputs':inputs, 'translated_inputs':(firstPlayWeight, secondPlayWeight)}

roundScores = []
rounds = []
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
            else:
                roundScores.append(result.get('loser_score'))
            count = count +1
if len(rounds) != len(roundScores):
    raise Exception('Rounds and rounds results don\'t match')
else:
    print(sum(roundScores))

