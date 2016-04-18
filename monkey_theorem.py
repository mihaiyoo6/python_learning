import random


def generate_sentance():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    sentance = ""
    while len(sentance) != 28:
        nr_random = random.randint(0, len(alphabet)-1)
        sentance += alphabet[nr_random]

    print(sentance)
    return sentance


def compare_sentence():
    goal = "methinks it is like a weasel"
    goal_len = len(goal)
    generated = generate_sentance()
    generated_len = len(generated)

    if goal_len != generated_len:
        print('sentence lengths are different')
        return True
    else:
        a = 0
        equalities = 0
        while a < goal_len:
            if goal[a] == generated[a]:
                equalities += 1

            a += 1
        score = equalities*100/28
        # print ("score ", score )
        return score


def run_theorem():
    count = 0
    big_procent = 0

    while count < 100000:
        procent = compare_sentence()
        if procent > big_procent:
            big_procent = procent
        count += 1

    return big_procent


print("run_theorem ", run_theorem())