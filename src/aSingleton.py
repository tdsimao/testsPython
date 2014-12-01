#!/usr/bin/env python
from lib.patterns import Singleton


class TestSingletone():
	__metaclass__ = Singleton

	def __init__(self):
		self.name = ''

	def set_name(self,n):
		self.name = n

	def get_name(self):
		return self.name
