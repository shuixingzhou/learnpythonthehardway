import random

times = 3
secret = random.randint(1,10)
guess = 0

print('========I love Python========')

print('Guess what number in my heart!',end=' ')

while(guess != secret) and (times >0):
	temp = input()
	while not temp.isdigit():
		temp = input('Not digit, enter again: ')
	guess = int(temp)
	times = times -1
	if guess == secret:
		print('Crazy, you are right!')
	else:
		if guess > secret:
			print('Bro, it\'s too big!')
		if guess < secret:
			print('Hey, it\'s too small.')
		if times > 0:
			print('You can have another try: ',end='')
		else:
			print('NO CHANCE')
print('GAME OVER')

