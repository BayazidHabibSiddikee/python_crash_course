import unittest
from name_function import get_name as GN #using Alias

class test(unittest.TestCase):
	def test_name(self):
		name = GN('janis','jopline')
		self.assertEqual(name,'Janis Jopline')
	def test_mid(self):
		name = GN('a','b','c')
		self.assertEqual(name,'A C B')

if __name__ == '__main__':
	unittest.main()
