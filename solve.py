#Written By Collin Lakeland.

#This is a program to solve any equation using Newton's Method.

#division module makes it so division operator doesn't round the  quotient
from __future__ import division
from decimal import *
#Imported for the valuable method float.is_integer
import numbers
#cmath module allows for complex operations and solutions
import cmath
import math
#sympy module allows for symbolic manipulation, and differentiation of special
#mathematical functions.
from sympy import *
import re
import sys
import time

#The imaginary number i = (-1)^0.5 = j in Python.
#Any number with a j appended to it is treated as a complex number by Python.
class Solver:

	def __init__(self, argv):
		pass

	def original_variables(self, argv):
		#User input; converted to complex type.
		#Initial coefficients and powers.
		self.args = argv
		self.sum_call_counter = 1
		self.power_rule_counter = 1
		self.conjugate_return = int()
		self.keyword = False
		#Results of substitution
		self.y = complex()
		#Results of power_rule
		self.o = complex()
		self.power_rule_list = [0]
		self.list_without_power_rule_operation = [0]
		self.powers = []	

	def prompter(self):
		print ("Hello, welcome to Collin's solver program!\n"
		"Note, your equation must be set equal to zero,\n"
		"and your guess must be fairly close to the root.\n" 
		"If you think a root is zero, then guess close to\n"
		"zero, but not actually zero.\n")
		self.guess = complex(input("Take a guess: "))

	
	#power_rule operation is used on coeffcient/power pairs, ex. elements 
	#at indexes (1,2),(3,4), etc.
	def power_rule_substitution(self):
		try:
			print "POWER RULE OUTPUT\n"
			#print "THE LENGTH OF ARGV IS {0}".format( len(self.args) )
			x = 1
			#Initial index value
			self.i = 2
			#Subtract initial argument, the program name, and divide it
			#by 2 to get the correct iterations
			self.argcounter = (len(self.args) - 1) / 2
			
			#For results of power_rule. 0 is a placeholder in this list
			
			while self.argcounter >= 0:
				#Stop appending once argcounter = 0.
				if self.argcounter == 0:
					break
				for arg in self.args:
					#print "p is", complex(self.args[self.i])
					#print "c is", complex(self.args[self.i-1])
					#print "x is", x
					#print "self.args index is %d" % self.i				
			
					#The call is odd.
					if self.power_rule_counter % 2 != 0:
						#Power rule operation
						#power * (corresponding coefficient * guess ^ (power - 1))
						self.o = complex(self.args[self.i]) * (
							complex(self.args[self.i-1]) * self.guess ** 
							(complex(self.args[self.i]) - 1 ) )
						
						print "self.o is {0}".format(self.o)
						self.power_rule_list.append(self.o)
	
					#The call is even.
					if self.power_rule_counter % 2 == 0:
						#Substitution, no power rule operation.
						self.y = complex( self.args[self.i-1] ) * self.guess ** ( 
							complex( self.args[self.i] ) )
						
						print "self.y is {0}".format(self.y)
						self.list_without_power_rule_operation.append(self.y)
					x += 1
					#Power elements
					self.i = 2*x
					self.argcounter -= 1
					#time.sleep(2)
					#print "argcounter is %d" % self.argcounter
					#When  the result is computed, break the for loop, go
					#back to the while loop and append each result into
					#new_list.
					break
			
			#This is supposed to prevent an infinite loop from occuring, while
			#allowing self.power_rule_substitution to be called a second time.
			if self.power_rule_counter % 2 != 0:
				#Do not change the order.
				
				self.power_rule_counter += 1
				self.power_rule_substitution()
			else:
				self.power_rule_counter += 1
		
		except ValueError as e:
			print 'The error is "{0}"'.format(e)
			print self.args
			i = 1
			#If any of the following keywords are found within argv use sympy 
			#methods.
			#print len(self.args)
			while i < len(self.args):
				#The 'r' isn't necessary but it is commonly used to denote a
				#regular expression pattern.
				if re.search( r'sin|cos|tan|sec|csc|cot|ln|log|sqrt|e|'
					'pi', self.args[i]):
						self.keyword = True
						#print "The keyword \"{0}\" is here.".format(self.args[i])
				else:
					print " \"{0}\" is not a keyword.".format(self.args[i])
				i += 1
	#Creates sympy object.
	def expression_creator(self):
		self.x = symbols('x')
		if self.keyword == True:
			x = 1
			argcounter = ( (len(self.args)) - 1 )/ 2
			self.expression_string = ""
			while argcounter > 0:
				i = 2*x
				x += 1
				#Creates the first part of a string using sympy syntax; it will
				#soon be turned into a sympy object.
				term = "{0}**{1}+".format(self.args[i-1], self.args[i])
				#Continuosly add terms to the string.
				self.expression_string += term
				#print self.expression_string
				argcounter -= 1
				#print argcounter

		#Strip the "+" on the end of the string.
		self.expression_string = self.expression_string.rstrip("+")
		print self.expression_string
		self.expr = sympify(self.expression_string)
		
	#Finds the derivative of the expression, and performs Newtons method on the
	#expression 1001 times.
	def special_Newtons_method(self):
		derivative = diff(self.expr, self.x)
		n = 1
		while n <= 1000:
			#"subs" substitutes in the initial self.guess for the deifned symbol
			#x.
			self.guess -= ( self.expr.subs(self.x, self.guess) /

				( derivative.subs(self.x, self.guess) ) )
			n += 1
		print "The final result of the SPECIAL Newton\'s method is", self.guess



	#This sums all the elements in list_without_power_rule_operation and
	#sums all the elements in new_list.
	def sum_method(self, data_list):
		print "SUM METHOD OUTPUT:\n"
		a = 2
		n = len(data_list) - 1
		print "LENGTH - 1 IS %d" % n
		
		#Add the first two elements.
		#complex is used because you could have complex numbers as input and
		#the elements must be converted from strings.
		self.sum = complex(data_list[a-1]) + complex(data_list[a])
		
		print "the initial sum is", self.sum
		while a <= n:
			a += 1
			#print "a is %d in sum" % a	
			#When a = n, then a = a+1, which is out of the list range. 
			#This prevents it from erroring.
			if a > n:
				print "a is greater than n in sum"
				break
			self.sum = ( self.sum + complex(data_list[a]) )
		
		#self.sum_call_counter is odd
		if self.sum_call_counter % 2 != 0:
			print "sum_counter is odd %d" % self.sum_call_counter
			self.substitution_list_sum = self.sum
			self.sum_call_counter += 1
			
		#self.sum_call_counter is even
		elif self.sum_call_counter % 2 == 0:
			print "sum_counter is even %d" % self.sum_call_counter
			self.power_rule_list_sum = self.sum
			self.sum_call_counter += 1
		print "THE FINAL SUM IS {0}\n".format(self.sum)

	#Applys the mathematical process called "Newton's method"
	#Finds the zeros correctly, but the guess MUST be near the zero. If two
	#zeros are 2 and -2, and the guess is 1, then it will give a solution of 2.
	#If the guess is -1, then it will give a solution of -2; it all depends on 
	#which zero is closer to the guess. 
	#Complex (imaginary) solutions require complex guesses.
	def Newtons_method(self):
		print "NEWTON OUTPUT:\n"
		n = 0
		while n <= 1000:
			self.guess = ( self.guess - 
			(self.substitution_list_sum/self.power_rule_list_sum) )
			n += 1                                                 
			#Repeat the process using the new self.guess, do this 1001 times
			#for a high degree of accuracy.
			self.iterate()
			#Reset the lists after an iteration of Newton's_method
			self.power_rule_list = [0]
			self.list_without_power_rule_operation = [0]
			#print "newton_counter IS %d" % n
			#print "The new self.guess is {0}".format(self.guess)
			#time.sleep(5)
			
		#The single result of Newton's
		print "THE FINAL RESULT OF NEWTON'S METHOD IS: {0}\n".format(self.guess)

	#Tests whether or not the result of Newton's Method is an actual solution 
	#to the equation, based on the user's guess, by seeing how close the 
	#equation is to zero. If it isn't very close, then the user should try 
	#another guess.
	def solution_tester(self):
		print "SOLUTION TESTER OUTPUT:\n"
		if self.keyword == False:
			#print "The power_rule counter is", self.power_rule_counter
			#As long as Newton's method is called 1001 times
			#self.power_rule_counter will always be 2005.
			#Add 1 to it so when power_rule_substitution is called
			#the final self.guess is substituted in.
			self.power_rule_counter += 1
			#print "Now the counter is {0}".format(self.power_rule_counter)
			#Cleaner way of doing this?
			self.list_without_power_rule_operation = [0]
			self.power_rule_substitution()
			self.sum_method(self.list_without_power_rule_operation)
			#print "The sum is {0}".format(self.sum)
			
			#If both the real and imaginary parts of the sum are between a very
			#small negative number and a very small positive number.
			#e(number), in this case, is equivalent to 10**number.
			if ( ( -1e-6 < self.sum.real < 1e-6 ) and
			
				( -1e-6 < self.sum.imag < 1e-6 ) ):
			
				print "VALID SOLUTION"			
			else:
				print ( "THE PROGRAM IS LYING TO YOU. Try another guess.\n"
				"Maybe make it complex (e.g. of the form a+bj)" )
				sys.exit()
		#if there are keywords
		elif -1e-6 < self.expr.subs(self.x, self.guess) < 1e-6:
			print "VALID SOLUTION"
		else:
			print ( "THE PROGRAM IS LYING TO YOU. Try another guess.\n"
				"Maybe make it complex (e.g. of the form a+bj)" )
			sys.exit()
			
	#IS THERE A CLEANER WAY OF WRITING THIS METHOD?
	#If both parts of the solution or one part are tiny, then they default to 
	#zero.
	def approximate(self):
		#To ensure self.guess has both real and imaginary parts, even if they
		#are zero.
		self.guess = complex(self.guess)
		if ( -1e-6 < (self.guess.real) < 1e-6 and 
			-1e-6 < (self.guess.imag) < 1e-6 ):
			
			self.guess = 0
			print ( "SELF.GUESS WAS APPROXIMATED IT NOW EQUALS {0}"
			.format(self.guess) )
		elif -1e-6 < (self.guess.real) < 1e-6:
			#This type of reassignment prevents TypeErrors.
			self.guess = complex(0, self.guess.imag)
			print ( "SELF.GUESS.REAL WAS APPROXIMATED IT IS {0}"
			.format(self.guess.real) )
		elif -1e-6 < (self.guess.imag) < 1e-6:
			self.guess = complex(self.guess.real, 0)
			print ( "SELF.GUESS.IMAG WAS APPROXIMATED IT IS {0}"
			.format(self.guess.imag) )
	
	def iterate(self):		
		#Repeat the process.
		#Parenthesis calls the method; it will not work without it.
		self.power_rule_substitution()
		self.sum_method(self.list_without_power_rule_operation)
		self.sum_method(self.power_rule_list)

	def reprompt(self):
		print "REPROMPT OUTPUT:\n"
		self.reprompt_return_value = 0
		if self.keyword == False and self.polynomial == True:
			while self.solutions > 0:
				if self.answers.count(self.guess) == 0:
					print "That is a new solution"
					self.answers.append(self.guess)
					self.solutions -= 1
						
					if self.conjugate == True:
						print "The conjugate is also a new solution."
						self.answers.append( complex(self.guess.real, 
							-1*self.guess.imag) )
	
						self.solutions -= 1
					else:
						print "The conjugate is not unique."
				else:
					print ("That solution has already been found,\n"
					"so it will not be added to self.answers.")
				print "The answers list is {0}".format(self.answers)
	
				print "REPROMPT OUTPUT:\n"
				print "There are %d solutions left.\n" % self.solutions
				
				if self.solutions == 0:
					break
				self.original_variables(sys.argv)
				self.prompter()
				#Call iterate to do the essential operations for Newton's method 
				#again.
				self.iterate()
				#Call Newton's method to work with the newly created data, and call
				#iterate a thousand more times.
				self.Newtons_method()
				self.solution_tester()
				self.approximate()
				self.answer_spitter()
				
		elif self.keyword == True:
			#The Fundamental Theorem of Algebra cannot be used, so just keeping
			#running until the user is done.
			while 1:
				if self.answers.count(self.guess) == 0:
					print "That is a new solution"
					self.answers.append(self.guess)
				else:
					print ("That solution has already been found,\n"
					"so it will not be added to self.answers.")
				print "The answers list is {0}".format(self.answers)
				self.original_variables(sys.argv)
				self.prompter()
				self.expression_creator()
				self.special_Newtons_method()
				print self.keyword
				self.solution_tester()
				self.approximate()
				self.answer_spitter()
				
		#self.keyword == False and self.polynomial == False
		else:
			while 1:
				if self.answers.count(self.guess) == 0:
					print "That is a new solution"
					self.answers.append(self.guess)
				else:
					print ("That solution has already been found,\n"
					"so it will not be added to self.answers.")
				print "The answers list is {0}".format(self.answers)
				self.original_variables(sys.argv)
				self.prompter()
				self.iterate()
				self.Newtons_method()
				self.solution_tester()
				self.approximate()
				self.answer_spitter()


	def answer_spitter(self):
		#Default bool value is False.
		self.conjugate = False
		print "ANSWER_SPITTER OUTPUT:\n"
		#If the imaginary part exists and all the coeffcients are real, 
		#then the conjugate also exists.
		if ( (self.guess.imag != 0 or self.guess.imag < -1e-6 or 
			self.guess.imag > 1e-6) and self.conjugate_return != 1 ):
			
			#print "This is a pure imaginary answer\n"
			print "The answer is {0}".format(self.guess)
			print "and the conjugate answer is {0} \n".format( -1*self.guess)
			self.conjugate = True
		else:
			print ("This solution doesn't have an imaginary part, so it has "
			"no\nconjugate answer.")


	#This is a work around; it sets variables that will only be reset once and
	#never again.
	def setter(self):
		self.reprompt_return_value = 1
		self.answers = []
	
	#If a polynomial has rational coefficients, and (a - sqrt(b)) is a root, 
	#then (a + sqrt(b)) is a root.
		
	#I think there is a better way to do this using the Fraction module and
	#passing in irrational numbers.


	def irrational_root_checker(self):
		print "IRRATIONAL ROOT CHECKER OUTPUT:\n"
		getcontext().prec = 30
		print "self.guess squared is",(self.guess)**2
		
	#If the input entered doesn't correspond to a polynomial, then NONE OF THE
	#FOLLOWING METHODS APPLY.
	def polynomial_checker(self):
		print "CHECKER OUTPUT:\n"
		self.polynomial = bool()
		self.i = 2
		b = 0
		#Is there a cleaner way of this reassignment to its initial value?
		self.argcounter = (len(self.args) - 1) / 2
		#Take all the powers from the user input, and put them in a list.
		while self.argcounter >= 0:
			self.powers.append(float(self.args[self.i]))
			self.i += 2
			self.argcounter -= 1
			if self.argcounter == 0:
				break
		print "powers is {0}".format(self.powers)
		#Gives the numbers after the decimal point, if any. In other words,
		#determines if the number is an integer in the mathematical sense,
		#Using int() on any float just cuts off the decimal portion 
		#of the number.
		for elements in self.powers:
			#print "Integer is", int(powers[b])
			a = self.powers[b] - int(self.powers[b])
			print "a is {0}".format(a)
			#The key piece of logic.
			if (self.powers[b] < 0 or a != 0.0 or type(self.powers[b])
			== complex):
				
				print ("This is not a polynomial,\n"
				"so the number of roots cannot be determined.")
				#THIS NEEDS TO BE CHANGED
				return
			b += 1
		self.polynomial = True

	#Uses the complex conjugate theorem: if a + b*j is a root, then a - b*j
	#is also a root.
	def conjugate_tester(self):
		print "CONJUGATE OUTPUT:\n"
		#Checks whether all of the coefficients are real, if not, this method
		# a condition in number_of_roots, and a condition in answer_spitter
		#doesn't apply.
		#Default value is 0.
		self.i = 1
		m = 0
		self.argcounter = (len(self.args) - 1 )/2
		while self.argcounter >= 0:
			print "The coefficients are:{0} \n".format(self.args[self.i])
			if complex(self.args[self.i]).imag != 0:
				print "Not all coeffcients are real\n"
				self.conjugate_return = 1
				return 1
			self.argcounter -= 1
			if self.argcounter == 0:
				break
			m += 1
			#self.i is always odd
			self.i = 2*m + 1
		print "All coeffcients are real."

	def number_of_roots(self):
		print "ROOT_NUMBER OUTPUT:\n"
		#If reprompt hasn't been called yet.
		if self.reprompt_return_value ==  1 and self.keyword == False:			
			self.solutions = max(self.powers)
		#Uses the Fundamental Theorem of Algebra to tell the user how many
		#roots there are.
		
		#If the leading power of a polynomial is odd and it has real 
		#coefficients, then it has at least one real root.
		
		if self.conjugate_return != 1 and self.solutions % 2 != 0:
		#I know I could have the condition like this, but is there anyway to
		#supress the output?
		#if self.complex_conjugate() != 1 and self.solutions % 2 != 0:
			print ("There are %d complex roots total, and at least 1 of them is"
			" real." % self.solutions)
		else:
			print ("I don't know how many real roots there are, but there are\n"
			"%d complex roots total.") % self.solutions
	

	def irrational_coefficient_checker(self):
		print "IRRATIONAL COEFFICIENT OUTPUT:\n"
		self.irrational = bool()
		x = 0
		i = 1
		#if it makes it through the for loop, then no coefficients are irrational
		for coefficient in self.args:
			self.args[i] = complex(self.args[i])
			print self.args[i]
			if ( float.is_integer(self.args[i].real) == False 
				or float.is_integer(self.args[i].imag) == False ):
				print "I errored"
				self.irrational = True
				return
			else:
				print "I didn't error"
				x  += 1
				i = 2*x + 1
				if i > len(self.args) -2:
					break	
		print "All coeffiecients are rational"


#The arguments 1 2 1 0 give ZeroDivisionError when the guess = 1, but works
#correctly when the guess = 1j

#SOMETIMES WHEN THE GUESS IS CLOSE TO 0 IT GIVES A COMPLEX SOLUTION, LIKE WITH
#ARGUMENTS 1 0.5 -15 3

#TODO: arguments 2 3 4 5 6 0.9 give zero division error when the guess isn't complex

#TODO: when they guess a number outside the domain, have it save their answers
#WHEN THEY ARE COMPLETELY DONE AND EXIT HAVE IT PRINT OUT THERE SOLUTIONS

#TODO: keyword argument errors in reprompt

#Work on the irrational number methods


solverObject = Solver(sys.argv)
solverObject.setter()
while 1:
	try:
		solverObject.__init__(sys.argv)
		solverObject.original_variables(sys.argv)
		solverObject.prompter()
		#All of these lines only get called once; reprompt handles all the
		#subsequent calls.
		solverObject.power_rule_substitution()
		if solverObject.keyword == True:
			solverObject.expression_creator()
			solverObject.special_Newtons_method()
		else:
			solverObject.sum_method(solverObject.power_rule_list)
			solverObject.sum_method(solverObject.list_without_power_rule_operation)
			solverObject.Newtons_method()
		
		solverObject.solution_tester()
		solverObject.approximate()
		
		#if reprompt hasn't been called yet
		if solverObject.reprompt_return_value == 1:
			if solverObject.keyword == False:
				#If there are no keywords, then the polynomial attribute is
				#created.
				solverObject.polynomial_checker()
				if solverObject.polynomial == True:
					solverObject.conjugate_tester()
					solverObject.number_of_roots()
				#solverObject.irrational_coefficient_checker()
		solverObject.answer_spitter()
		solverObject.reprompt()
		
	except ZeroDivisionError:
		print ("\nERROR MESSAGE:\n\n Oops, it looks like your guess was zero, "
		"or not in\nthe function's domain. Guess again. Maybe make it complex, "
		"real,\n or a pure imaginary number. Hit \"control-C\""
		"to exit.\n Please wait....\n")
		time.sleep(5)
		continue
	except KeyboardInterrupt:
		print "\n\nYour solutions are {0}\n\nBye".format(solverObject.answers)
		sys.exit()



#Useless code, right now:


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
