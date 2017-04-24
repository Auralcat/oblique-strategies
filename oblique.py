#/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Oblique Strategies for the command line
   Just run the script and it returns a card."""

import random

def getStrategies():
    with open("./src/edition_1.txt") as stratfile:
        strategies = [line.strip('\n') for line in stratfile.readlines()]
    return strategies

def callStrategy():
    print(random.choice(getStrategies()))

callStrategy()
