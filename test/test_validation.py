import unittest

from nhs import validate

class test_validation(unittest.TestCase):


	def test_valid_numbers(self):
		"""
			Test to ensure validation works on a range of valid formats
		"""
		l = ['999 999 9468','999-999-9484', ' 999 999 9514 ', '9999999565']
		for i in l:
			try:
				response, checksum = validate(i)
				self.assertNotEquals(10, checksum)
				self.assertTrue(response)
			except ValueError:
				self.fail('None of these tests should fail.')


	def test_validation_short(self):
		"""
			Tests to ensure validation works on short numbers
		"""
		l = '0123456'
		self.assertRaises(ValueError, validate, l)


	def test_validation_long(self):
		"""
			Tests to ensure validation works on long numbers
		"""
		l = '0101010101010'
		self.assertRaises(ValueError, validate, l)


	def test_validation_extra_chars(self):
		"""
			Tests to ensure the method can accept NHS numbers with
			hypens or spaces.
		"""
		l = '012-012-0321'
		validate(l)
		self.assertTrue(True)


	def test_validation_alpha(self):
		"""
			Test to ensure validation fails on alpha characters
		"""
		l = '123456789a'
		self.assertRaises(ValueError, validate, l)


if __name__ == '__main__':
    unittest.main()