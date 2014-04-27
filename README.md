lakelandcol
===========
This is for a program called "Collin's polynomial solver", written by 
Collin Lakeland in Python.
 .........
To use this program in a productive way (this is NOT guaranteed by the
developer) the user must SET THE EQUATION EQUAL TO ZERO, otherwise the SOLVER 
program cannot SOLVE for the zeros. You must also enter the coefficients 
and corresponding powers of those coefficients as arguments to the program name. 
For example, the equation,

3x^2 + 4x + 1 = 0

would be entered in as:
	3 2 4 1 1 0
	
Notice how even when the power is 0 or 1 you still must enter it, in
order to be productive that is. When you enter your coefficients and powers
you should always have to enter an even number of them, otherwise you probably 
did something wrong.
WARNING: white space (i.e. spaces) is considered an argument

For an equation like,

x^2 - 3x +4x^(-3) = 0

you would enter them in as:
	1 2 -3 1 4 -3

Notice how when you have negative coefficients or powers you must signify 
that with the negative sign attached to it, just like in math class.

As a tip, if the coefficient is 0, or the term is ommitted, (for instance the
equation x^2 + 1, could be written as x^2 + 0x + 1, although this becomes 
tedious) then the coefficient, and therefore corresponding power, may also be 
ommitted when putting in your arguments.

The guess MUST be near the zero. For example, if two zeros are 2 and -2, 
and the guess is 1, then it will give a solution of 2. If the guess is -1,
then it will give a solution of -2; it all depends on which zero is closer
to the guess.

Also, if the zero is complex (contains i), then your guess must also be complex,
for a real guess is not close to a complex guess.

To make sure you never obtain an erroneous solution, make sure your guess is not
a pure imaginary number. (i.e. 3j, 5j) Make sure it has a real part to it, like
3j+4.

NOTE: A guess of j (= i) would be input as 1j; the 1 signifies that it is a
complex number and not a string.

I DO NOT ENDORSE OR SUPPORT USING THIS AS A CRUTCH IN MATH CLASS, IN FACT 
I DESPISE IT. SOLVE YOUR OWN PROBLEMS! ATTEMPT TO USE THIS PROGRRAM TO AID 
YOU IN MATHEMATICAL DISCOVERY.
