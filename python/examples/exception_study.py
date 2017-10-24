#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Networkerror(Exception):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror, argument:
    print argument.args  # 输出: ('B', 'a', 'd', ' ', 'h', 'o', 's', 't', 'n', 'a', 'm', 'e')


def throw_excep(var):
    print "function start..."
    raise Exception("you win", var)


try:
    throw_excep("abcd")
except Exception:
    print "catch exception"
else:
    print "no problem."


def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "reason: ", Argument


temp_convert("abc")  # 输出：reason:  invalid literal for int() with base 10: 'abc'