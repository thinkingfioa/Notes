#!/usr/bin/python
# -*- coding: UTF-8 -*-

Money = 2000


def add_money():
    #global Money
    Money = Money + 200


print Money  # 输出：2000
add_money()
print Money  # 输出：2200