import math

year = input()
holidays = int(input())
h = int(input())

weekend_sofia = 48  * 0.75 
play_sofia = weekend_sofia + (holidays * 0.666)
play_total = play_sofia + (h / 2)

if year == 'leap':
    play_total = play_total + (play_total * 0.15)
else:
    play_total = play_total
print(math.floor(play_total))