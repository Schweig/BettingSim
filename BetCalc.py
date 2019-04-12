def calc(bet,line):
    sign  = line[0]
    winnings =0
    if sign is '+':
        val = line[1:]
        dec = int(val)/100
        final = dec +1
        winnings = final*bet
    elif sign is '-':
        val = line[1:]
        dec = 100/int(val)
        final = dec+1
        winnings = final*bet
    return winnings-bet

print(calc(100,'+120'))
