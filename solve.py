#Written By Collin Lakeland

#Program to solve any equation using Newton's Method

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
		#Debigging
		#print self.args
		self.func_call_counter = 1

		
	#power_rule method is used on coeffcient/power pairs, ex. elements 
	#at (1,2),(3,4), etc.
	
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
		

	#TODO: The creation of new_list should be another method, but I
	#don't know how to do that, because the elements (self.o) will constantly
	#get updated.


	
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
	
	

	def sum(self, data_list):
		print "sum_substitution output:\n"
		print "list_without_operation is", data_list
		
		#This sums all the elements in the substitution list.
		#func_call_counter keeps track of the number of function calls
		a = 2
		n = len(data_list) - 1
		print "initial n is %d" % n
		#Add the first two elements.
		#float is used because you could have decimals as input and the elements
		#must be converted from strings.
		
		#Outer parentheses are used because the line is broken; they keep the
		#operation contained
		sum = float(data_list[a-1]) + float(data_list[a])
		
		print "the initial sum is %f" % sum
		while a <= n:
			a += 1
			print "a is %d" % a	
			#When a = n, then a = a+1, which is out of the list range. 
			#This prevents it from erroring.
			if a > n:
				print "a is greater than n"
				break
			print "a is %d" % a
			
			sum = ( sum + float(data_list[a]) )

		if self.func_call_counter == 1:
			self.substitution_list_sum = sum
		elif self.func_call_counter == 2:
			self.new_list_sum = sum
			
			print "the current sum is %f\n"
		print "The final sum is %f\n" % sum
		

		#TODO: Shouldn't be copied and pasted, maybe have it loop through each
		#list, or should it be a new method?
		#This sums all the elements in new_list
	"""
		print "This is the output for new_list:\n"
		a = 2
		n = len(self.new_list) - 1
		print "initial n is %d" % n
		#Add the first two elements.
		#float is used because you could have decimals as input and the elements
		#must be converted from strings.
		
		self.new_list_sum = self.new_list[a-1] + self.new_list[a]
		
		print "the initial sum for new_list is is %f" % self.new_list_sum
		while a <= n:
			a += 1
			print "a is %d" % a
			#When a = n, then a = a+1, which is out of the list range. 
			#This prevents it from erroring.
			if a > n:
				#Debugging
				print "a is greater than n"
				break
			print "a is %d" % a
			
			self.new_list_sum = self.new_list_sum + float(self.new_list[a])
			print "the current sum for new_list is %f\n" % self.new_list_sum
		print "The final sum for new_list is %f\n" % self.new_list_sum
	"""
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
			#time.sleep(5)
			#print "n is %d" % n
			#Repeat the process using the new self.guess; do this 10001 times
			#for a high degree of accuracy
			#Parenthesis calls the method, will not work without it.
			self.power_rule()
			self.substitution()
			self.sum()
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
