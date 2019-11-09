import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):

	def setUp(self):
		self.new_user = User('Dancan','Od\'uo\'r','28750d')

def test__init__(self):
		self.assertEqual(self.new_user.first_name,'Dancan')
		self.assertEqual(self.new_user.last_name,'Od\'uo\'r')
		self.assertEqual(self.new_user.password,'28750d')

def test_save_user(self):
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)