#!usr/bin/env python3
#-*- coding: utf-8 -*-

def fab(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n + 1

for n in fab(6):
	print(n)

def fab1(max):
	n,a,b = 0,0,1
	result = []
	while n < max:
		result.append(b)
		a,b =b, a+b
		n +=1
	return result

print(fab1(6))

for n in fab1(6):
	print(n)

