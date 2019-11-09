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
	def test_check_user(self):
		self.new_user = User('Dancan','Od\'uo\'r','28750')
		self.new_user.save_user()
		user2 = User('Ben','Od\'uo\'r','28750d')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))
		return current_user

		

	def setUp(self):
		self.new_credential = Credential('Dancan','Facebook','dancanoduor','28750d')

	def test__init__(self):
		self.assertEqual(self.new_credential.user_name,'Dancan')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'dancanoduor')
		self.assertEqual(self.new_credential.password,'28750d')

	def test_save_credentials(self):
		self.new_credential.save_credentials()
		twitter = Credential('Dancan','Twitter','dancanoduor','28750d')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

	def tearDown(self):
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		self.new_credential.save_credentials()
		twitter = Credential('Dancan','Twitter','dancanoduor','28750d')
		twitter.save_credentials()
		gmail = Credential('Dancan','Gmail','dancanoduor','28750d')
		gmail.save_credentials()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

	def test_find_by_site_name(self):
		self.new_credential.save_credentials()
		twitter = Credential('Dancan','Twitter','dancanoduor','28750d')
		twitter.save_credentials()
		credential_exists = Credential.find_by_site_name('Twitter')
		self.assertEqual(credential_exists,twitter)

	def test_copy_credential(self):
		self.new_credential.save_credentials()
		twitter = Credential('Dancan','Twitter','dancanoduor','28750d')
		twitter.save_credentials()
		find_credential = None
		for credential in Credential.user_credentials_list:
				find_credential =Credential.find_by_site_name(credential.site_name)
				return pyperclip.copy(find_credential.password)
		Credential.copy_credential(self.new_credential.site_name)
		self.assertEqual('28750d',pyperclip.paste())
		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)