# bowling game
score1 = [(8,0), (4,3), (4,6), (2,6), (10,0), (9,0), (10,0), (8,2), (10,0),(10,10)]
score2 = [(10,0), (10,0), (10,0),(10,0), (10,0), (10,0),(10,0), (10,0), (10,0),(10,0),(10,10)]


def bowling(score):
    total = i = 0
    frame = []
    for first, second in score:
        f_total = first+second
        if i != 9:
            next_first, next_second = score[i+1]
        if first == 10:
            result = 'STRIKE'
            f_total += next_first + next_second
            if i < 8 and next_first == 10:
                next_next_first, next_next_second = score[i+2]
                f_total += next_next_first
        elif (first+second)==10:
            result = 'SPARE'
            f_total += next_first
        else: result = 'NONE'
        total += f_total
        frame.append((f_total, result))
        i += 1
        if i == 10: break
    print(frame)
    print("Total = ", total)
    print()

bowling(score1)
bowling(score2)

