lakelandcol
===========
This is for a program called "Collin's Solver", Written by 
Collin Lakeland in Python.
 .........
To use this program in a productive way (this is NOT guaranteed by the
developer) the user must SET THE EQUATION EQUAL TO ZERO before entering it,
otherwise the SOLVER program cannot SOLVE for the zeros. You must also
enter the coefficients (with a "*x" at the end of them) and corresponding powers
of those coefficients as arguments to the program name. For example, the
equation,

3x^2 + 4x + 1 = 0

would be entered in as:
	3*x 2 4*x 1 1*x 0
	
Notice how even when the power is 0 or 1 you still must enter it, in
order to be productive that is. When you enter your coefficients and powers
you should always have to enter an even number of them, otherwise you probably 
did something wrong.

If special keywords, like "log", "sin", "cos", etc involve parentheses
make sure a backslash preceeds each parenthesis.

WARNING: white space (i.e. spaces) is considered an argument
WARNING: you must input at LEAST 4 arguments. So for something like

sin(5*x) = 0

you would do

sin\(5*x\)*x 0 0*x 0
This is equivalent to

sin(5*x)*x^0 + 0*x^0 = sin(5*x)*1 + 0

For an equation like,

x^2 - 3x + 4x^(-3) = 0

you would enter it in as:
	1*x 2 -3*x 1 4*x -3

Notice how when you have negative coefficients or powers you must signify 
that with the negative sign attached to it, just like in math class.

As a tip, if the coefficient is 0, or the term is ommitted, (for instance the
equation x^2 + 1, could be written as x^2 + 0x + 1, although this becomes 
tedious) then the coefficient, and therefore corresponding power, may also be 
ommitted when putting in your arguments. That is of course unless you have less
than 4 arguments with this omission, in which case you shouldn't omit it.

The guess MUST be near the zero. For example, if two zeros are 2 and -2, 
and the guess is 1, then it will give a solution of 2. If the guess is -1,
then it will give a solution of -2; it all depends on which zero is closer
to the guess.

Also, if the zero is complex (contains i), then your guess must also be complex,
for a real guess is not close to a complex guess.


NOTE: A guess of j (= i) would be input as 1j; the 1 signifies that it is a
complex number and not a string.

I DO NOT ENDORSE OR SUPPORT USING THIS AS A CRUTCH IN MATH CLASS, IN FACT 
I DESPISE IT. SOLVE YOUR OWN PROBLEMS! ATTEMPT TO USE THIS PROGRRAM TO AID 
YOU IN MATHEMATICAL DISCOVERY.
