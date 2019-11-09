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

class TestCredentials(unittest.TestCase):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Dancan','Od\'uo\'r','28750')
		self.new_user.save_user()
		user2 = User('Oduor','Od\'uo\'r','28750d')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))
		return current_user

		

def setUp(self):
		'''
		
		'''
		self.new_credential = Credential('Dancan','Facebook','Dancanoduor','28750d')

def test__init__(self):
		self.assertEqual(self.new_credential.user_name,'Dancan')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'dancanoduor')
		self.assertEqual(self.new_credential.password,'28750187')

def test_save_credentials(self):
		self.new_credential.save_credentials()
		twitter = Credential('Dancan','Twitter','dancanoduor','28750187')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

def tearDown(self):
		Credential.credentials_list = []
		User.users_list = []