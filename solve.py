#Written By Collin Lakeland.

#This is a program to solve any equation using Newton's Method.

#division module makes it so division operator doesn't round the 
#quotient
from __future__ import division

#cmath module allows for complex solutions, may or may not be necessary
#at this point
import cmath
import sys
import time

class Solver:

	def __init__(self, argv):
		print ("Hello, welcome to Collin's solver program!\n"
		"Note your equation must be set equal to zero,\nand your guess "
		"must be fairly close to the root.")
		
		#User input; converted input to float.
		self.guess = float(input("Take a guess: "))
		#Initial coefficients and powers.
		self.args = argv

		#b helps count the number of sum method calls
		self.b = 1

		
	#power_rule method is used on coeffcient/power pairs, ex. elements 
	#at indexes (1,2),(3,4), etc.
	
	def power_rule(self):
		print "power_rule output:\n"
		#For results of power_rule. 0 is a placeholder.
		self.o = float()
		self.new_list = []
		x = 1
		#initial n value
		n = 2
		#Subtract initial argument, the program name, and divide it
		#by 2 to get the correct iterations
		argcounter = (len(self.args) - 1) / 2
		
		while argcounter >= 0:
			#TODO: should this be placed elsewhere in the method?
			self.new_list.append(self.o)
			#Stop appending once argcounter = 0.
			if argcounter == 0:
				break
			for arg in self.args:
			
				print "p is %d" % float(self.args[n])
				print "c is %d" % float(self.args[n-1])
				print "x is %d" % x
				print "n is %d" % n
				
				#power * (corresponding coefficient * guess ^ (power - 1))
				#convert list elements to integers
				self.o = float(self.args[n]) * ( float(self.args[n-1]) * 
				self.guess ** ( float(self.args[n]) - 1 ) ) 
				
				x += 1
				#Power elements
				n = 2*x
				argcounter -= 1
				#%f is the string formatter for REAL, floating numbers.
				#This may cause problems later on with complex solutions.
				print "argcounter is %f" % argcounter
				print "result is %f" % self.o
				#When  the result is computed, break the for loop, go
				#back to the while loop and append each result into
				#new_list.
				break
		#TODO: string formatting for lists?
		print "new_list is\n", self.new_list


	
	#Doesn't apply power_rule operation just substitutes self.guess into the
	#original coefficients and corresponding powers (argv).
	def substitution(self):
		print "substitution output:\n"
		self.y = float()
		x = 1
		n = 2
		self.list_without_power_rule_operation = []
		argcounter = (len(self.args) - 1) / 2
		
		while argcounter >= 0:
			self.list_without_power_rule_operation.append(self.y)
			#Stop appending once argcounter = 0.
			if argcounter == 0:
				break
			for arg in self.args:
				
				print "p is %d" % float(self.args[n])
				print "c is %d" % float(self.args[n-1])
				print "x is %d" % x
				print "n is %d" % n
				
				self.y = float( self.args[n-1] ) * self.guess ** ( 
				float( self.args[n] ) )
				
				x += 1
				#Power elements
				n = 2*x
				argcounter -= 1
				print "argcounter is % f" % argcounter
				print "self.y is % f" % self.y
				#When  the result is computed, break the for loop, go
				#back to the while loop and append each result into
				#new_list.				
				break
		print "substitution list is\n", self.list_without_power_rule_operation
	
	
	#This sums all the elements in list_without_power_rule_operation and
	#sums all the elements in new_list.
	def sum(self, data_list):
		print "sum method output:\n"
		#print "list_without_operation is", data_list		
		a = 2
		n = len(data_list) - 1
		print "initial n is %d" % n
		#Add the first two elements.
		#float is used because you could have decimals as input and the elements
		#must be converted from strings.
		
		sum = float(data_list[a-1]) + float(data_list[a])
		
		print "the initial sum is %f" % sum
		while a <= n:
			a += 1
			print "a is %d" % a	
			
			#when self.b is odd
			if self.b % 2 != 0:
				self.substitution_list_sum = sum
				print "b is %d" % self.b
			
			#when self.b is even
			elif self.b % 2 == 0:
				self.new_list_sum = sum
				print "b is %d" % self.b
			self.b += 1
			
			#When a = n, then a = a+1, which is out of the list range. 
			#This prevents it from erroring.
			if a > n:
				print "a is greater than n"
				break
				
			print "a is %d" % a
			sum = ( sum + float(data_list[a]) )
			
			print "the current sum is %f\n" % sum

		print "This is", self.b % 2 
		print "The final sum is %f\n" % sum


	#Applys the mathematical process called "Newton's method"
	#Finds the zeros correctly, but the guess MUST be near the zero. If two
	#zeros are 2 and -2, and the guess is 1, then it will give a solution of 2.
	#If the guess is -1, then it will give a solution of -2; it all depends on 
	#which zero is closer to the guess.
	def Newtons_method(self):
		print "Output for Newton's method:\n"
		n = 0
		while n <= 1000:
			self.guess = ( self.guess - 
			(self.substitution_list_sum/self.new_list_sum) )
			n += 1
			#time.sleep(10)
			print "n is %d" % n
			#Repeat the process using the new self.guess; do this 10001 times
			#for a high degree of accuracy.
			#Parenthesis calls the method, will not work without it.
			self.power_rule()
			self.substitution()
			self.sum(self.list_without_power_rule_operation)
			self.sum(self.new_list)
		print "The answer is %f" % self.guess

#TODO: Work on finding the other zeros, or on making the process of finding the
#other zeros easier for the user; maybe prompt them?

solverObject = Solver(sys.argv)
solverObject.power_rule()
solverObject.substitution()
solverObject.sum(solverObject.list_without_power_rule_operation)
solverObject.sum(solverObject.new_list)
solverObject.Newtons_method()

#Pseudocode

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
