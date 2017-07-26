#!/usr/bin/env python
# coding=utf-8

def print_hello(name, sex):
    sex_dict = {1: u'先生', 2: u'女士'}
    print( 'hello %s %s, welcome to python world!' %(name, sex_dict.get(sex, u'先生')))


# 两个参数的顺序必须一一对应，且少一个参数都不可以
print_hello('tanggu', 2)
