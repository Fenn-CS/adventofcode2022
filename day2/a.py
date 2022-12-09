file1 = open("input", "r")
score = 0

data = {
        "X": 1,
        "A": 1,
        "Y": 2,
        "B": 2,
        "Z": 3,
        "C": 3
}

def win(a, b):
        if a == b:
                return 0
        if a == 1 and b == 2:
                return -1
        if a == 1 and b == 3:
                return 1
        if a == 2 and b == 1:
                return 1
        if a == 2 and b == 3:
                return -1
        if a == 3 and b == 1:
                return -1
        if a == 3 and b == 2:
                return 1


count = 1
while True:
        line = file1.readline()
        if not line:
                break
        line = line.strip().split()
        i, j = line
        a, b = data[i], data[j]
        print("Round {} inputs are ({}, {})".format(count, a, b))
        if win(b, a) > 0:
                score += b + 6
                print("Round {} score {}".format(count, b+6))
        elif win(b, a) == 0:
                score += b + 3
                print("Round {} score {}".format(count, b+3))
        else:
                score += b
                print("Round {} score {}".format(count, b))
        print("Total score: {}".format(score))
        count = count + 1

print(score)
