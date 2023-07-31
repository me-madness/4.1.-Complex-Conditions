city = input()
money = float(input())
result = 0

if not (city == 'Sofia' or city == 'Plovdiv' or city == 'Varna'):
    print('error')
else:
    if city == 'Sofia':
        if money >= 0 and money <= 500 :
            result = (money / 100) * 5
        elif money > 500 and money <= 1000:
            result = (money / 100) * 7
        elif money > 1000 and money <= 10000:
            result = (money / 100) * 8 
        else:
            result = (money / 100) * 12         
    elif city == 'Plovdiv':
        if money >= 0 and money <= 500 :
            result = (money / 100) * 5.5
        elif money > 500 and money <= 1000:
            result = (money / 100) * 8
        elif money > 1000 and money <= 10000:
            result = (money / 100) * 12 
        else:
            result = (money / 100) * 14.5         
    else:
        if money >= 0 and money <= 500 :
            result = (money / 100) * 4.5
        elif money > 500 and money <= 1000:
            result = (money / 100) * 7.5
        elif money > 1000 and money <= 10000:
            result = (money / 100) * 10 
        else:
            result = (money / 100) * 13         
    print(round(result, 2))      