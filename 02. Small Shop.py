product = input().lower()
city = input().lower()
quantity = float(input())

result = 0

if city == 'sofia':
    if product == 'coffee':
        result = quantity * 0.50
    elif product == 'water':    
        result = quantity * 0.80
    elif product == 'beer':    
        result = quantity * 1.20
    elif product == 'sweets':    
        result = quantity * 1.45
    else :    
        result = quantity * 1.60
elif city == 'plovdiv':
    if product == 'coffee':
        result = quantity * 0.40
    elif product == 'water':    
        result = quantity * 0.70
    elif product == 'beer':    
        result = quantity * 1.15
    elif product == 'sweets':    
        result = quantity * 1.30
    else :    
        result = quantity * 1.50
else:
    if product == 'coffee':
        result = quantity * 0.45
    elif product == 'water':    
        result = quantity * 0.70
    elif product == 'beer':    
        result = quantity * 1.10
    elif product == 'sweets':    
        result = quantity * 1.35
    else :    
        result = quantity * 1.55
print(round(result, 2))            