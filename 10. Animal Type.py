animal = input()
result = ''
if animal == 'dog':
    result = 'mamal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    result = 'reptile'  
else:
    result = 'unknown'  
print(result)        