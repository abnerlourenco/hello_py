# -*- coding: utf -8 -*-

class Calculadora:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def soma(self):
		resultado = self.a + self.b
		self.impressao(resultado)

	def subtracao(self):
		resultado = self.a - self.b
		self.impressao(resultado)

	def impressao(self, a):
		print(a)