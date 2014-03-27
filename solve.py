#Written By Collin Lakeland
#Program to solve any equation using Newton's Method


#division module makes it so division operator doesn't round the 
#quotient
from __future__ import division
#cmath module allows for complex solutions, may or may not be necessary
#at this point
import cmath
import sys

class Solver:

	def __init__(self, argv):
		#User input
		self.guess = int()
		self.args = argv
		#Debigging
		print self.args
		#print self.args.index('1')
		#print self.args.index('2')
		#print self.args.index('3')
		
	#power_rule method is used on coeffcient/power pairs, ex. elements 
	#at (1,2),(3,4), etc
	
	def power_rule(self):
		
		for arg in self.args:
			x = 1
			#Power elements
			n = 2*x
			#Subtract initial argument, the program name, and divide it 
			#by 2 to get the correct iterations
			argcounter = (len(self.args)-1)/2
			print "p is", int(self.args[n])
			print "c is", int(self.args[n-1])
			if argcounter < 0:
				
				break
			#power * corresponding coefficient ^ (power - 1)
			#convert list elements to integers
			#TODO: If I try and break this line it errors
			o = int(self.args[n])*int(self.args[n-1])**int(self.args[n]) - 1
			x += 1
			argcounter -= 1
		
		print argcounter
		print o

		#Useless code and comments, at the moment.
		
		"""
		numbers = []
		c = 1
		x = 1
		#subtract 0th argument
		argtotal = len(sys.argv)-1
		#User enters even number of arguments
		#argcounter is also the number of iterations needed for correct 
		#coeffcient/power placement
		final_iteration = argtotal/2
		initial_iteration = 0
		#print argtotal, argcounter

		print "initial coef place is %d\n" % c
		while final_iteration > initial_iteration:
			for arg in self.args:

				#power
				p = 2*x
				#coefficient
				x = x + 1
				initial_iteration = initial_iteration + 1
				#Debugging
				print "power place is ", p
				print "x is", x
				print "iteration = ", initial_iteration
				#coefficient
				c = p + 1
				#if the coeff place is > the total arguments break the 
				#for loop, occurs when final_iteration = 
				#initial_iteration, so the while loop is also broken
				if c > argtotal:
					break
				print "coeff place is %d\n" % c
				
				break
				
				FIX: Doesn't print out an extra coeffcient place, but 
				the assignment is still taking place
		
				FIX: convert list arguments to integers maybe using for
				loop
				
		MAYBE INSERT A 0 AT THE BEGINNING OF SELF.ARGS TO GET CORRECT
		INDEXING AND PLACEMENT?
		
		MAYBE USE THIS?
	
		n = 0
		print self.args
		print len(self.args)
		for args in self.args:
			if n > len(self.args):
				break
			numbers.append(self.args[n])
			n = n + 1
				"""
solverObject = Solver(sys.argv)
solverObject.power_rule()
	
	
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
