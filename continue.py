#!usr/bin/python3
#Filename: continue.py

while True:
	s = input('Enter sth:')
	if s == 'quit':
		break
	if len(s) != 4:
		print('length is wrong')
		continue
	print('length is right')
	# Do other kinds of processing here...
