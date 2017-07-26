from random import choice

print('Choose one side to shoot:')
print('Left','Center','Right')
you = input('Direction:')
print('You kicked ', you)
direction = ['Left','Center','Right']
com = choice(direction)
if you != com:
	print('Goal')
else:
	print('Oops..')
