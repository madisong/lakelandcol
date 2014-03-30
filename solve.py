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
		print ("Hello, welcome to Collin's solver program!\n"
		"Note your equation must be set equal to zero,\nand your guess "
		"must be fairly close to the root.")
		
		#User input; converted input to integer.
		self.guess = int(input("Take a guess: "))
		#Initial coefficients and powers.
		self.args = argv
		#Debigging
		print self.args
		
	#power_rule method is used on coeffcient/power pairs, ex. elements 
	#at (1,2),(3,4), etc.
	
	def power_rule(self):
		#For results of power_rule. o is initially a placeholder.
		self.o = 'solver.py'
		new_list = []
		x = 1
		#initial n value
		n = 2
		#Subtract initial argument, the program name, and divide it 
		#by 2 to get the correct iterations
		argcounter = (len(self.args) - 1) / 2
		
		while argcounter >= 0:
	
			new_list.append(self.o)
			#Stop appending once argcounter = 0.
			if argcounter == 0:
				break
			for arg in self.args:
			
				print "p is %d" % int(self.args[n])
				print "c is %d" % int(self.args[n-1])
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
		print "new_list is", new_list
		
	#TODO: The creation of new_list should be another method, but I
	#don't know how to do that, because the results (self.o) constantly
	#get updated.
	
	#def new_coeff_power_list(self):
		
	
	def Newtons_method(self):
		#This sums all the elements in the initial list (argv).
		a = 2
		n = len(self.args) - 1
		#Add the first two elements.
		#float is used because you could have decimals as input
		sum = float(self.args[a-1]) + float(self.args[a])
		print "the initial sum is %f" % sum
		while a <= n:
			a += 1
			#When a = n, a then = a+1, which is out of the list range. 
			#This prevents it from erroring.
			if a > n:
				break
			print "a is %d" % a
			sum = sum + float(self.args[a])
			print "the current sum is %f\n" % sum
		print "The final sum is %f" % sum
	

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
solverObject.Newtons_method()

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
