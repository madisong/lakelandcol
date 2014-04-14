#Written By Collin Lakeland.

#This is a program to solve any equation using Newton's Method.

#division module makes it so division operator doesn't round the  quotient
from __future__ import division

#cmath module allows for complex operations and solutions
import cmath
import sys
import time

#the imaginary number  i = j in Python
#Any number with a j appended to it is treated as a complex number by Python.
class Solver:

	def __init__(self, argv):
		print ("Hello, welcome to Collin's solver program!\n"
		"Note your equation must be set equal to zero,\nand your guess "
		"must be fairly close to the root.")
		
		#User input; converted to complex type.
		self.guess = complex(input("Take a guess: "))
		#Initial coefficients and powers.
		self.args = argv
		self.sum_call_counter = 1
		self.power_rule_counter = 1
		#results of substitution
		self.y = complex()
		#results of power_rule
		self.o = complex()
		#power_rule method is used on coeffcient/power pairs, ex. elements 
		#at indexes (1,2),(3,4), etc.		
		self.new_list = []
		self.list_without_power_rule_operation = []
	
	def power_rule_substitution(self):
		x = 1
		#initial n value
		n = 2
		print "power_rule_substitution output:\n"
		print "The initial power counter value is\n", self.power_rule_counter
		if self.power_rule_counter % 2 == 0:
			print "The counter is even and:\n"
			print "x is",x
			print "n is", n
		#Subtract initial argument, the program name, and divide it
		#by 2 to get the correct iterations
		argcounter = (len(self.args) - 1) / 2
		
		#For results of power_rule. 0 is a placeholder in this list
		
		while argcounter >= 0:
			#Stop appending once argcounter = 0.
			if argcounter == 0:
				break
			for arg in self.args:
			
				print "p is", complex(self.args[n])
				print "c is", complex(self.args[n-1])
				print "x is", x
				print "n is ", n				
				#the call is odd
				if self.power_rule_counter % 2 != 0:
					#power rule operation
					#power * (corresponding coefficient * guess ^ (power - 1))
					#convert list elements to integers
					self.o = float(self.args[n]) * ( float(self.args[n-1]) * 
					self.guess ** ( float(self.args[n]) - 1 ) )
					print "self.o is", self.o
					self.new_list.append(self.o)

				#the call is even
				if self.power_rule_counter % 2 == 0:
					#substitution, no power rule operation
					self.y = float( self.args[n-1] ) * self.guess ** ( 
					float( self.args[n] ) )
					print "self.y is", self.y
					self.list_without_power_rule_operation.append(self.y)
				x += 1
				#Power elements
				n = 2*x
				argcounter -= 1
				print "argcounter is %d" % argcounter
				#print "result is", self.o
				#When  the result is computed, break the for loop, go
				#back to the while loop and append each result into
				#new_list.
				break
		print "The new value is\n", self.power_rule_counter
		print "new_list is\n", self.new_list
		
		#This is supposed to prevent an infinite loop from occuring, while
		#allowing self.power_rule_substitution to be called a second time.
		if self.power_rule_counter % 2 != 0:
			self.power_rule_counter += 1
			self.power_rule_substitution()
			print "substitution list is", self.list_without_power_rule_operation
		else:
			self.power_rule_counter += 1
	#Doesn't apply power_rule operation just substitutes self.guess into the
	#original coefficients and corresponding powers (argv).
	"""
	def substitution(self):
		print "substitution output:\n"
		x = 1
		n = 2
		argcounter = (len(self.args) - 1) / 2
		
		while argcounter >= 0:
			#Stop appending once argcounter = 0.
			#Contradicts the while condtion because self.y must be appended even
			#when argcounter equals 0
			if argcounter == 0:
				break
			for arg in self.args:
				
				print "p is", complex(self.args[n])
				print "c is", complex(self.args[n-1])
				print "x is", x
				print "n is", n
				
				self.y = float( self.args[n-1] ) * self.guess ** ( 
				float( self.args[n] ) )
				
				x += 1
				#Power elements
				n = 2*x
				argcounter -= 1
				print "argcounter is %d" % argcounter
				print "self.y is", self.y
				#When  the result is computed, break the for loop, go
				#back to the while loop and append each result into
				#new_list.				
				break
		print "substitution list is\n", self.list_without_power_rule_operation
	"""
	
	
	#This sums all the elements in list_without_power_rule_operation and
	#sums all the elements in new_list.
	def sum(self, data_list):

		print "sum method output:\n"
		#print "list_without_operation is", data_list		
		a = 2
		n = len(data_list) - 1
		print "initial n is %d" % n
		#Add the first two elements.
		#complex is used because you could have complex numbers as input and
		#the elements must be converted from strings.
		
		sum = complex(data_list[a-1]) + complex(data_list[a])
		
		print "the initial sum is", sum
		while a <= n:
			a += 1
			print "a is %d" % a	
			#When a = n, then a = a+1, which is out of the list range. 
			#This prevents it from erroring.
			if a > n:
				print "a is greater than n"
				break
			print "a is %d" % a
			sum = ( sum + complex(data_list[a]) )
			
			print "the current sum is \n", sum

		#print "This is", self.sum_call_counter % 2
		#when self.sum_call_counter is odd
		if self.sum_call_counter % 2 != 0:
			print "b is odd", self.sum_call_counter
			self.substitution_list_sum = sum
			self.sum_call_counter += 1
			
		#when self.sum_call_counter is even
		elif self.sum_call_counter % 2 == 0:
			print "b is even", self.sum_call_counter
			self.new_list_sum = sum
			self.sum_call_counter += 1
		print "The final sum is \n", sum

	#Applys the mathematical process called "Newton's method"
	#Finds the zeros correctly, but the guess MUST be near the zero. If two
	#zeros are 2 and -2, and the guess is 1, then it will give a solution of 2.
	#If the guess is -1, then it will give a solution of -2; it all depends on 
	#which zero is closer to the guess.
	def Newtons_method(self):
		print "Output for Newton's method:\n"
		n = 0
		#If this wasn't here it would error, because self.new_list_sum doesn't
		#exist yet. May not be necessary now.
		#self.sum(self.new_list)
		while n <= 1000:
			self.guess = ( self.guess - 
			(self.substitution_list_sum/self.new_list_sum) )
			n += 1
			print "N IS", n
			time.sleep(10)
			#print "n is %d" % n
			#Repeat the process using the new self.guess; do this 1001 times
			#for a high degree of accuracy.
			#Parenthesis calls the method, will not work without it.
			self.power_rule_substitution()
			#self.substitution()
			self.sum(self.list_without_power_rule_operation)
			self.sum(self.new_list)
			print "Continuation of Newton's method Output:\n"
			print "The new self.guess is", self.guess
			continue

		if self.guess.imag == 0:
			print "This is a pure real answer\n"
			print "The answer is", self.guess.real

		else:
			print "This is a complex answer\n"
			print "The answer is", self.guess

#TODO: Making the process of finding the other zeros easier for the user; 
#maybe prompt them?


#The arguments 1 2 1 0 give ZeroDivisionError when the guess = 1, but works
#correctly when the guess = 1j

#SOMETIMES WHEN THE GUESS IS CLOSE TO 0 IT GIVES A COMPLEX SOLUTION, LIKE WITH
#ARGUMENTS 1 0.5 -15 3

#FREQUENT ZERO DIVISON ERRORS ESPECIALLY WHEN 0 IS THE GUESS

#TODO: DO NOT FORGET ABOUT THE COMPLEX CONJUGATES THEOREM

solverObject = Solver(sys.argv)
solverObject.power_rule_substitution()
#solverObject.substitution()
solverObject.sum(solverObject.list_without_power_rule_operation)
print solverObject.sum_call_counter
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
