hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]
change =[1,'pennies',2,'dimes',3,'quarters']
print(hairs)
print(hairs[0])

fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for fruit in fruits:
	print('A fruit of type: %s' % fruit)

for i in change:
	print('I got %r' % i)

elements =[]
for i in range(0,6):
	print('Adding %d to the list.' % i)
	elements.append(i)
	print(elements)

for i in elements:
	print('Element was: %d' % i)
