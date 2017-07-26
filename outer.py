#/usr/bin/env python3

def outer():
	a = 0
	b = 1
 
	def inner():
#		b = 4
		print(a)
		print(b)
        # b += 1        # A
		b = 4
	inner()

outer()
