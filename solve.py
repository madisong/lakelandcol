#Written By Collin Lakeland.

#This is a program to solve any equation using Newton's Method.

#division module makes it so division operator doesn't round the  quotient
from __future__ import division
from decimal import *
from special import *
#Imported for the valuable method float.is_integer
#import numbers
#cmath module allows for complex operations and solutions
import cmath
import math
import re
import sys
import time
import pygame
import os



#The imaginary number i = (-1)^0.5 = j in Python.
#Any number with a j appended to it is treated as a complex number by Python.
class Solver(Special):

	def __init__(self, argv):
		self.reprompt_return_value = 1
		self.answers = []
		self.real_coefficients = False

	
	def original_variables(self, argv):
		#User input; initial coefficients and powers.
		self.args = argv
		self.power_rule_counter = 1
		#Only used within sum_method, but it is necessary that it not be set
		#to its initial value in that method.
		self.sum_call_counter = 1
		self.power_rule_list = [0]
		self.list_without_power_rule_operation = [0]
		self.powers = []
		self.valid = True

	def prompter(self):
		print ( "Hello, welcome to Collin's solver program!\n"
		"Note, your equation must be set equal to zero,\n"
		"and your guess must be fairly close to the root.\n" 
		"If you think a root is zero, then guess close to\n"
		"zero, but not actually zero.\n\n" 
		"Enter the coefficients and corresponding powers of your equation.\n"
		"Make sure each term in the equation has \"*x\" attached to it.\n"
		"A backslash should preceed any parentheses.\n\n"
		"For example, 3x^2 + tan(3x) -4 would be entered in as:\n"
		"3*x 2 tan\(3*x\)*x 0 -4*x 0")
		self.guess = complex(input("Take a guess: "))

	
	#power_rule operation is used on coeffcient/power pairs, ex. elements 
	#at indexes (1,2),(3,4), etc.
	def power_rule_substitution(self):
		try:
			#self.special_args is a duplicate of self.args, but the coefficients
			#don't have the "*x" stripped, so that sympy can work with that data
			self.special_args = []
			
			#Results of substitution
			y = complex()
			#Results of power_rule
			o = complex()
			a = 0
			b = 0
			while a <= (len(self.args) - 1):
				self.special_args.append(self.args[a])
				self.args[a] = self.args[a].rstrip("*x")

				a += 1
			print "POWER RULE OUTPUT\n"
			x = 1
			#Initial index value
			i = 2
			#Subtract initial argument, the program name, and divide it
			#by 2 to get the correct iterations
			self.argcounter = (len(self.args) - 1) / 2

			while self.argcounter > 0:
				#for arg in self.args:
					#print "p is", complex(self.args[self.i])
					#print "c is", complex(self.args[self.i-1])
					#print "x is", x
					#print "self.args index is %d" % self.i				
			
				#The call is odd.
				if self.power_rule_counter % 2 != 0:
					#Power rule operation
					#power * (corresponding coefficient * guess ^ (power - 1))
					o = complex(self.args[i]) * (
						complex(self.args[i-1]) * self.guess ** 
						(complex(self.args[i]) - 1 ) )
					
					print "o is {0}".format(o)
					self.power_rule_list.append(o)

				#The call is even.
				if self.power_rule_counter % 2 == 0:
					#Substitution, no power rule operation.
					y = complex( self.args[i-1] ) * self.guess **( 
						complex( self.args[i] ) )
					
					print "y is {0}".format(y)
					self.list_without_power_rule_operation.append(y)
				x += 1
				#Power elements
				i = 2*x
				self.argcounter -= 1
				#print "argcounter is %d" % self.argcounter
				self.keyword = False
			
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
			#If any of the following keywords are found within argv use sympy 
			#methods.
			#print len(self.args)
			for elements in self.special_args:
				#The 'r' isn't necessary but it is commonly used to denote a
				#regular expression pattern.
				if re.search( r'sin|cos|tan|sec|csc|cot|ln|log|sqrt|math.e|'
					'math.pi', elements):
						self.keyword = True
						self.polynomial = False
						print ( "The keyword \"{0}\" is here."
							.format(elements) )
				else:
					print ( " \"{0}\" is not a keyword.".format(elements) )


	#This sums all the elements in self.list_without_power_rule_operation and
	#sums all the elements in self.power_rule_list.
	def sum_method(self, data_list):
		print "SUM METHOD OUTPUT:\n"
		a = 2
		n = len(data_list) - 1
		print "LENGTH - 1 IS %d" % n
		print "POWER RULE LIST", self.power_rule_list
		print "SUBSTITUTION  LIST", self.list_without_power_rule_operation
		#Add the first two elements.
		#complex is used because you could have complex numbers as input and
		#the elements must be converted from strings.
		self.sum = complex(data_list[a-1]) + complex(data_list[a])
		
		print "the initial sum is", self.sum
		while a < n:
			print a
			a += 1
			self.sum += complex(data_list[a])
			#time.sleep(2)
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
	#If two zeros are 2 and -2, and the guess is 1, then it will give a solution
	#of 2.If the guess is -1, then it will give a solution of -2; it all depends
	#on which zero is closer to the guess. Complex (imaginary)
	#solutions require complex guesses.
	def Newtons_method(self):
		print "NEWTON OUTPUT:\n"
		n = 0
		while n <= 1000:
			self.guess -= (
				(self.substitution_list_sum/self.power_rule_list_sum) )
			n += 1                                                 
			#Repeat the process using the new self.guess, do this 1001 times
			#for a high degree of accuracy.
			self.iterate()
			#Reset the lists after an iteration of Newton's_method
			self.power_rule_list = [0]
			self.list_without_power_rule_operation = [0]
		#Rounding is used to prevent the appendation of answers that have tiny
		#differences
		self.guess = ( complex(round(self.guess.real, 7),
			round(self.guess.imag, 7)) )

		print "THE FINAL RESULT OF NEWTON'S METHOD IS: {0}\n".format(self.guess)

	#Tests whether or not the result of Newton's Method is an actual solution 
	#to the equation, based on the user's guess, by seeing how close the 
	#equation is to zero. If it isn't very close, then the user should try 
	#another guess.
	def solution_tester(self):
		print "SOLUTION TESTER OUTPUT:\n"
		#print self.keyword
		
		if self.keyword == False:
			#As long as Newton's method is called 1001 times
			#self.power_rule_counter will always be 2005.
			#Add 1 to it so when power_rule_substitution is called
			#the final self.guess is substituted in.
			self.power_rule_counter += 1
			#Cleaner way of doing this?
			self.list_without_power_rule_operation = [0]
			self.power_rule_substitution()
			self.sum_method(self.list_without_power_rule_operation)
			
			#If both the real and imaginary parts of the sum are between a very
			#small negative number and a very small positive number.
			#e(number), in this case, is equivalent to 10**number.
			if ( ( -1e-6 < self.sum.real < 1e-6 ) and
			
				( -1e-6 < self.sum.imag < 1e-6 ) ):
			
				print "VALID SOLUTION"
			else:
				self.valid = False

		#if there are keywords
		elif (-1e-6 < self.expr.subs(self.x, self.guess) < 1e-6 ):
			print self.expr.subs(self.x,self.guess)
			print "VALID SOLUTION"
			time.sleep(5)
		else:
			self.valid = False

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
		self.power_rule_substitution()
		self.sum_method(self.list_without_power_rule_operation)
		self.sum_method(self.power_rule_list)

	def reprompt(self):
		self.reprompt_return_value = 0
		
		print "REPROMPT OUTPUT:\n"		
		if self.polynomial == True:
			
			while self.solutions > 0:
				os.system("clear")
				if self.valid == True and self.answers.count(self.guess) == 0:
					pygame.mixer.init()
			
					sound = pygame.mixer.Sound("ding.wav")	
					sound.play()
					print "That is a new solution"
					self.answers.append(self.guess)
					self.solutions -= 1
						
					if ( self.real_coefficients == True and 
						self.guess.conjugate() != self.guess ):
						
						print "The conjugate is also a new solution."
						self.answers.append( self.guess.conjugate())
	
						self.solutions -= 1
					else:
						print "The conjugate is not unique."

				elif self.valid == False:
					print ( "THE PROGRAM IS LYING TO YOU. Try another guess.\n"
						"Maybe make it complex (e.g. of the form a+bj)\n\n Your"
						" current solutions are:\n\n {0}".format(self.answers) )
					pygame.mixer.init()
			
					sound = pygame.mixer.Sound("NO.wav")	
					sound.play()

				else:
					print "That solution has already been found,\n"
					
				print "The answers list is {0}\n".format(self.answers)
	
				print "There are %d solutions left.\n" % self.solutions

				if self.solutions == 0:
					print "All solutions found"	
					sys.exit()

				#Reset all the initial variables.
				self.original_variables(sys.argv)
				
				#Prompt and ask for another guess.
				self.guess = complex(input("Take a guess: "))
				
				#Call iterate to do the essential operations for Newton's method 
				#again.
				self.iterate()
				#Call Newton's method to work with the newly created data, and
				#call iterate a thousand more times.
				self.Newtons_method()
				self.solution_tester()
				self.approximate()
		else:
			#The Fundamental Theorem of Algebra cannot be used, so just keeping
			#running until the user is done.
			while 1:
				os.system("clear")
				if self.valid == True and self.answers.count(self.guess) == 0:
					pygame.mixer.init()
			
					sound = pygame.mixer.Sound("ding.wav")	
					sound.play()
					print "That is a new solution\n"
					self.answers.append(self.guess)
				elif self.valid == False:
					print ( "THE PROGRAM IS LYING TO YOU. Try another guess.\n"
						"Maybe make it complex (e.g. of the form a+bj)\n\n Your"
						" current solutions are:\n\n {0}".format(self.answers) )
					pygame.mixer.init()
			
					sound = pygame.mixer.Sound("NO.wav")	
					sound.play()
					
				else:
					print "That solution has already been found,\n"
					
				print "The answers list is {0}\n".format(self.answers)

				self.original_variables(sys.argv)
				self.guess = complex(input("Take a guess: "))
				if self.keyword == True:
					self.expression_creator()
					self.special_Newtons_method()
				else:
					self.iterate()
					self.Newtons_method()
				self.solution_tester()
				self.approximate()


	#THIS METHOD ISN'T BEING USED RIGHT NOW
	
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
		self.polynomial = False
		i = 2
		b = 0
		self.argcounter = (len(self.args) - 1) / 2
		#Take all the powers from the user input, and put them in a list.
		while self.argcounter > 0:
			self.powers.append(float(self.args[i]))
			i += 2
			self.argcounter -= 1
		print "powers is {0}".format(self.powers)
		#Gives the numbers after the decimal point, if any. In other words,
		#determines if the number is an integer in the mathematical sense,
		#Using int() on any float cuts off the decimal portion 
		#of the number.
		for elements in self.powers:
			#print "Integer is", int(powers[b])
			a = self.powers[b] - int(self.powers[b])
			print "a is {0}".format(a)
			#The key piece of logic.
			if (self.powers[b] < 0 or a != 0.0 or type(self.powers[b])
			== complex):
				
				print "This is not a polynomial"
				return
			b += 1
		self.polynomial = True

	#Tests to see if the complex conjugate theorem (if a + b*j is a root,
	#then a - b*j is also a root.) can be applied.
	def real_coefficent_tester(self):
		print "REAL_COEFFICIENT_TESTER OUTPUT:\n"
		#If this returns, then a condition in number_of_roots doesn't apply.
		i = 1
		m = 0
		self.argcounter = (len(self.args) - 1 )/2
		while self.argcounter > 0:
			print "The coefficients are:{0} \n".format(self.args[i])
			if complex(self.args[i]).imag != 0:
				print "Not all coeffcients are real\n"
				return
			self.argcounter -= 1
			m += 1
			i = 2*m + 1
		print "All coeffcients are real."
		self.real_coefficients = True

	#Uses the Fundamental Theorem of Algebra to tell the user how many
	#roots there are.
	def number_of_roots(self):
		print "ROOT_NUMBER OUTPUT:\n"
		
		if self.reprompt_return_value ==  1 and self.keyword == False:			
			self.solutions = max(self.powers)
	
	#THIS METHOD ISN'T BEING USED RIGHT NOW
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
				time.sleep(5)
				self.irrational = True
				return
			else:
				print "I didn't error"
				x  += 1
				i = 2*x + 1
				if i > len(self.args) -2:
					break
		print "All coeffiecients are rational"
		time.sleep(5)


#TODO: Bring in refactored solution_tester from SOLVE~.PY

#Work on the irrational number methods

#Object creation is separate because there are variables within __init__ that
#only need to be reset once, whereas, the variables in original_variables need
#to be reset many times.
solverObject = Solver(sys.argv)
while 1:
	try:
		solverObject.original_variables(sys.argv)
		solverObject.prompter()
		#All of these lines only get called once (if it doesn't error,
		#otherwise they will get called more than once);reprompt handles all
		#the subsequent calls.

		solverObject.power_rule_substitution()
		if solverObject.keyword == True:
			solverObject.expression_creator()
			solverObject.special_Newtons_method()
		else:
			solverObject.sum_method(solverObject.list_without_power_rule_operation)
			solverObject.sum_method(solverObject.power_rule_list)
			solverObject.Newtons_method()
		
		solverObject.solution_tester()
		solverObject.approximate()
		
		#if reprompt hasn't been called yet
		if solverObject.reprompt_return_value == 1:
			if solverObject.keyword == False:
				#If there are no keywords, then self.polynomial may be
				#reassigned; its set to False by default in
				#self.power_rule_substitution
				solverObject.polynomial_checker()
				if solverObject.polynomial == True:
					solverObject.irrational_coefficient_checker
					solverObject.real_coefficent_tester()
					solverObject.number_of_roots()
		solverObject.reprompt()
		
	except ZeroDivisionError:
		print ("\nERROR MESSAGE:\n\n Oops, it looks like your guess was zero, "
		"or not in\nthe function's domain. Guess again. Maybe make it complex, "
		"real,\n or a pure imaginary number. Hit \"control-C\""
		"to exit.\n Please wait....\n")
		time.sleep(5)
		continue
	
	except KeyboardInterrupt:
		os.system("clear")
		print ( "Your solutions are:\n\n{0}\n\nBye\n"
			.format(solverObject.answers) )
	
		sys.exit()