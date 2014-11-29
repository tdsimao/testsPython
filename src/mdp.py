#!/usr/bin/env python
import cProfile
from random import random,seed
from multiplyMatrix import *
import logging
from logging import debug
#import re


class MDP:
    S = []
    A = []
    P = []
    R = []
    gamma = 0.9


def grid():
	m = createMatrix(3,4, f = zero)
	m[0][3] = 1
	m[1][3] = -1
	m[2][1] = None
	return m


def main(i = 2,j = 1,k = 2):
	logging.basicConfig(filename='example.log',level=logging.DEBUG)
	logging.info('\n\n%s\nStarting Execution', 50*'*')
	debug('Some debug')
	#logging.warning('And this, too')
	
	logging.info('\n\n%s\nFinishe Execution', 50*'*')
	print grid()


main()

#cProfile.run('main(100,100,300)')

