#!usr/bin/python3
#Filename:if.py

number = 23
guess = int(input('Enter an integer:'))

if guess == number:
	print("Congratulations, you guessed it.")
	print('But you do not win any prizes!')
elif guess < number:
	print('No, higher')
else:
	print('No, lower')

print('Done')
