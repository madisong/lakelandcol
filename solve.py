#Written By Collin Lakeland

#Program to solve any equation using Newton's Method

from __future__ import division 		#division module makes it so the division operator doesn't round the quotient
import cmath                           #cmath module allows for complex solutions
import sys

class Solver:

	def __init__(self, argv):
		self.guess = int()
		self.o = []
		self.args = argv
		print self.args
	
	def coeff_power_placement(self):
		numbers = []
		c = 1
		x = 1
		#subtract 0th argument
		argtotal = len(sys.argv)-1
		#User enters even number of arguments
		#argcounter is also the number of iterations needed for correct coeffcient/power placement
		final_iteration = argtotal/2
		initial_iteration = 0
		#print argtotal, argcounter
		
		print "initial coef place is", c
		print
		while final_iteration > initial_iteration:
			for arg in self.args:
				#x = x + 1  #Reassign x
				#power
				p = 2*x
				#coefficient
				x = x + 1
				initial_iteration = initial_iteration + 1
				print "power place is ", p
				print "x is", x
				print "iteration = ", initial_iteration
				c = p + 1
				#if the coeff place is > the total arguments break the for loop, occurs when final_iteration = initial_iteration, so the while loop is also broken
				if c > argtotal:
					break
				print "coeff place is ", c

				#Debugging				
				print
				
				break
				
				#FIX: Doesn't print out an extra coeffcient place, but the assignment is still taking place on line 42, line 44 prevents the printing of it though. Will this be a problem later on?    Return may help fix this?

		#MAYBE USE THIS?

		n = 0
		for args in self.args:
			numbers.append(self.args[n])
			n = n + 1
		print numbers
			
			
solverObject = Solver(sys.argv[1:])
solverObject.coeff_power_placement()
	
	
	#print guess
	
	#self.o = sys.argv[c]*sys.argv[p]
	
		
	#def power_rule(self, coeffs, powers):

	#def Newtons_method(self, equation, guess):
	

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
