import unittest
from survey import Anonymous as AN

class test(unittest.TestCase):
	def setUp(self):
		qn = 'What language did u learn first'
		self.survey = AN(qn)
		self.response=['English','Spanish','Mandarin']
		
	def test_single(self):
		self.survey.store_res(self.response[0])
		self.assertIn(self.response[0],self.survey.response)
		
	def test_store_three_responses(self):
		for r in self.response:
			self.survey.store_res(r)
		for r in self.response:
			self.assertIn(r, self.survey.response)
if __name__ == '__main__':
	unittest.main()
