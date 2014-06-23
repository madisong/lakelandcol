from sympy import *


class Methods:
	#Creates sympy object.
	def expression_creator(self):
		print self
		self.x = symbols('x')
		x = 1
		argcounter = ( (len(self.special_args)) - 1 )/ 2
		self.expression_string = ""
		while argcounter > 0:
			i = 2*x
			x += 1
			#Creates the first part of a string using sympy syntax.
			term = ( "{0}**{1}+"
				.format(self.special_args[i-1], self.special_args[i]) )
	
			#Continuosly add terms to the string.
			self.expression_string += term
			#print self.expression_string
			argcounter -= 1
			#print argcounter
	
		#Strip the "+" on the end of the string.
		self.expression_string = self.expression_string.rstrip("+")
		print self.expression_string
		#time.sleep(10)
		self.expr = sympify(self.expression_string)
	
	#Finds the derivative of the expression, and performs Newtons method on the
	#expression 1001 times.
	def Newtons_method(self):
		derivative = diff(self.expr, self.x)
		n = 1
		while n <= 1000:
			#"subs" substitutes in the initial self.guess for the deifned symbol
			#x.
			self.guess -= ( self.expr.subs(self.x, self.guess) /
	
				( derivative.subs(self.x, self.guess) ) )
			n += 1
		#N is a rounding function in sympy
		#self.guess = round(self.guess, 6)
		print "The final result of the SPECIAL Newton\'s method is", self.guess
		self.guess = round(self.guess, 7)


MethodObject = Methods()