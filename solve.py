#Written By Collin Lakeland

#Program to solve any equation using Newton's Method

from __future__ import division 		#division module makes it so the division operator doesn't round the quotient
import cmath                           #cmath module allows for complex solutions
import sys

class Solver:

	def __init__(self, argv):
		#power
		#coefficient
		self.guess = int()
		self.o = []
		self.args = argv
		#print argv
		#print type(argv)
		# User enters four arguments
		#argtotal = len(sys.argv)-1 # should be 4
		#argcounter = argtotal / 2
		#print argtotal, argcounter
	
	def power_rule(self):
		x = 1
		i = 2*x
		j = 1
		for arg in self.args:
			#self.o = sys.argv[j]*sys.argv[i]
			x = x + 1
			j = i + 1
			print "value of x is ",  x
			print "value of i is ", i           #I ISNT RIGHT
			print "value of j is ",  j
solverObject = Solver(sys.argv[1:])
solverObject.power_rule()
		#print self.o
		#print guess
	#def power_rule(self, coeffs, powers):
	#def derivative(self, equation):


	#def Newtons_method(self, equation, guess):

solverObject = Solver(sys.argv[1:])

"""

Define the derivative of the equation

print "Now take a guess, your guess must be close to what the solution actually is"

**They guess**

Process ( guess - (equation)/(derivative) ) in a loop a high number of times, for a high degree of accuracy    **Newton's Method**

Store solution

print "Your solution is", solution

Repeat this process until all solutions are found    If the highest degree is an integer, then the number of solutions will equal this integer (when double roots are included)

print "Your solutions are:", solution1, solution2, solution3....solution-N  **Possibly in a column**

"""

"""
foo['key'] = {'key' : 'value'}
{0: {1:5}, 1: {3:4}}
print foo[0]
{1:5}
for coef, pwr in foo[0]:
	print coef
	print pwr
"""
