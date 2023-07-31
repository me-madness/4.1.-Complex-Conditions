movie_type = input().lower()
rows = int(input())
columns = int(input())

places = rows * columns
income = 0

if movie_type == 'premiere':
    income = places * 12.00
elif movie_type == 'normal':
    income = places * 7.50
else:
    income = places * 5.00
print(round(income, 2))          