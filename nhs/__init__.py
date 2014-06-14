"""
	Validates NHS Numbers
"""
# License: MIT (http://www.opensource.org/licenses/mit-license.php)

__version__ = '2.0.0'
__author__ = "Matt Seymour <matt@mattseymour.net>"

import re

def validate(nhs_number):
	"""
		Checks a given NHS numbers <string> is valid.
		@Returns: is_valid<bool>
	"""
	# Nhs number is sometimes inputted xxx-xxx-xxxx, lets strip this down
	nhs_number = re.sub('[- ]', '', nhs_number)

	# A valid NHS number must be 10 digits long
	if not re.search(r'^[0-9]{10}$', nhs_number):
		raise ValueError('NHS number must be a string 10 digits long.')

	checkcalc = lambda sum: 11 - (sum % 11)

	l = [int(j) * (10 - (i+1)) for i, j in enumerate(nhs_number[:-1])]
	checksum = checkcalc(sum(l)) if checkcalc(sum(l)) != 11 else 0

	return False if checksum == 10 else True
