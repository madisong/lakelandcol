"""stuff = 'an example word:cat!!\nCollin loves Lexi'

match = re.search(r'!$', stuff, re.X|re.M )

#If-statement after search() tests if it succeeded
print match
if match:
	print "Found '{0}'".format(match.group()) #found word:cat

if match == None:
	print "Didn\'t find the pattern you wanted"
"""    
import re
programming = ["Bash", "Python", "Perl", "PHP", "C++","Pascal", "Python","Beer	"]

pat = "Bash|^P|i$|\+$"

for lang in programming:
	
	if re.search(pat,lang,re.I):
		print "{0} FOUND".format(lang)
	else:
		print lang, "NOT FOUND"
print re.search(pat,lang,re.I)

