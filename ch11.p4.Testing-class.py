import unittest
from survey import Anonymous as AN

class test(unittest.TestCase):
	def test_single(self):
		qn = 'What language did u learn first'
		survey = AN(qn)
		survey.store_res('English')
		self.assertIn('English',survey.response)
if __name__ == '__main__':
	unittest.main()


#U can try with list too
