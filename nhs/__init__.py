# License: MIT (http://www.opensource.org/licenses/mit-license.php)


__version_info__ = (1, 0, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "Matt Seymour <mattaseymour@gmail.com>"

import re

def validate(nhs_number):
	"""
		Checks a given NHS numbers <string> is valid.
		@Returns: tuple(is_valid<bool>, checksum<int>)
	"""
	# Nhs number is sometimes inputted xxx-xxx-xxxx, lets strip this down
	nhs_number = re.sub('[- ]', '', nhs_number)

	# A valid NHS number must be 10 digits long
	if not re.search(r'^[0-9]{10}$', nhs_number):
		raise ValueError('NHS number must be a string 10 digits long.')

	checkcalc = lambda sum: 11 - (sum % 11)
	checkdigit = nhs_number[-1]

	l = [int(j) * (10 - (i+1)) for i, j in enumerate(nhs_number[:-1])]
	checksum = checkcalc(sum(l)) if checkcalc(sum(l)) != 11 else 0

	return False if checksum == 10 else True, checksum