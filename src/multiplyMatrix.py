#!/usr/bin/env python
import cProfile
from random import random,seed
import re


def zero():
	return 0

def createVector(x,f = lambda : random()):
	v = []
	for i in xrange(x):
		v.append(f())
	return v	


def createMatrix(x, y, f=lambda : random()):
	m = []
	for i in xrange(x):
		m.append(createVector(y, f))
	return m

def mult(a,b):
	i,j = len(a),len(b[0])
	c = createMatrix(len(a),len(b[0]),f = zero)
	for i in xrange(len(a)):
		for j in xrange(len(b[0])):
			for k in range(len(b)):
				c[i][j] += a[i][k] * b[k][j]

	return c

def main(i = 2,j = 1,k = 2):
	#seed()
	
	a = createMatrix(i,j)
	b = createMatrix(j,k)
	print a
	print b
	c = mult(a,b)

#main()

#cProfile.run('main(100,100,300)')

#for a in xrange(0):
#	print random()
