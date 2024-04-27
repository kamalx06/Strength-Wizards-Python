import random

stats = []
attributes = 5

print('Stats: ', end='')

for i in range(attributes):
	r = random.randint(60, 80)
	stats.append(r)
	print(stats[i], end=' ')

print('\n\t[1] - Strength\
\n\t[2] - Dexterity\
\n\t[3] - Intelligence\
\n\t[4] - Wisdom\
\n\t[5] - Charisma')

select = int(input('Select: '))
select -= 1
stats[select] = stats[select] + random.randint(5, 15)

for i in range(len(stats)):
	if i == select:
		continue
	stats[i] = stats[i] - random.randint(5, 15)
print('Stats: ', end='')
for i in range(attributes):
	print(stats[i], end=' ')

print('\n\t[6] - Fireball\
\n\t[7] - Lightning\
\n\t[8] - Silence\
\n\t[9] - Fireward')
fireball = 6
lightning = 7
silence = 8
fireward = 9
fireball = [12, 15, 28, 10, 5]
lightning = [7, 13, 15, 30, 10]
silence = [23, 10, 12, 7, 18]
fireward = [20, 23, 14, 6, 17]
attribute = 5
select2 = int(input('Select: '))

for b in range(len(stats)):
    if select2 == 6:
      stats[b] = stats[b] - 12, 15, 28, 10, 5
    elif select2 == 7:
      stats[b] = stats[b] - 7, 13, 15, 30, 10
    elif select2 == 8:
      stats[b] = stats[b] - 23, 10, 12, 7, 18
    elif select2 == 9:
      stats[b] = stats[b] - 20, 23, 14, 6, 17

print('Stats: ', end='')
for b in range(attribute):
	print(stats[b], end=' ')

