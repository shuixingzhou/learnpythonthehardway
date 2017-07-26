#!/usr/bin/env python  
  
a = 1  
print a.__class__  
print issubclass(a.__class__, object) # all objects in Python inherit from a common baseclass  
  
def foo():  
    pass  
  
print foo.__class__ # 1  
print issubclass(foo.__class__, object) 
