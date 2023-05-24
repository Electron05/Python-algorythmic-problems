import math
answers = []
T = int(input())
for i in range(T):
    a = int(input())
    if a == 0:
        answers.append(0)
        answers.append(0)
        continue
    if a == 1:
        answers.append(0)
        answers.append(1)
        continue

    log = math.floor(math.log2(a))
    diff = a - 2 ** log
    mod = log % 8
    a = 2 ** log
    if mod == 0:
        x, y = 0, int(math.sqrt(a))
    elif mod == 1:
        x, y = int(math.sqrt(a/2)), int(math.sqrt(a/2))
    elif mod == 2:
        x, y = int(math.sqrt(a)), 0
    elif mod == 3:
        x, y = int(math.sqrt(a / 2)), int(-math.sqrt(a / 2))
    elif mod == 4:
        x, y = 0, int(-math.sqrt(a))
    elif mod == 5:
        x, y = int(-math.sqrt(a / 2)), int(-math.sqrt(a / 2))
    elif mod == 6:
        x, y = int(-math.sqrt(a)), 0
    elif mod == 7:
        x, y = int(-math.sqrt(a / 2)), int(math.sqrt(a / 2))

    Invert = True
    a = diff
    while a >= 2:
        diffl = log - math.floor(math.log2(a))
        log = math.floor(math.log2(a))
        diff = a - 2 ** log
        mod = log % 8
        a = 2 ** log
        if Invert:
            mod += 4
            if mod > 7:
                mod -= 8
        if mod == 0:
            y += int(math.sqrt(a))
        elif mod == 1:
            x += int(math.sqrt(a / 2))
            y += int(math.sqrt(a / 2))
        elif mod == 2:
            x += int(math.sqrt(a))
        elif mod == 3:
            x += int(math.sqrt(a/2))
            y -= int(math.sqrt(a/2))
        elif mod == 4:
            y -= int(math.sqrt(a))
        elif mod == 5:
            y -= int(math.sqrt(a / 2))
            x -= int(math.sqrt(a / 2))
        elif mod == 6:
            x -= int(math.sqrt(a))
        elif mod == 7:
            x -= int(math.sqrt(a / 2))
            y += int(math.sqrt(a / 2))
        a = diff
        if diffl > 1 and Invert:
            Invert = False
        elif diffl > 1 and not Invert:
            Invert = True
    if a == 1:
        if Invert:
            y -= 1
        else:
            y += 1
    answers.append(x)
    answers.append(y)
for i in range(len(answers)):
    if i % 2 == 1:
        print(answers[i])
    else:
        print(answers[i], end=" ")