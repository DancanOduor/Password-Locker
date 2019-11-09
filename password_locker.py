import pyperclip
from user_credentials import User, Credential

def create_user(fname,lname,password):
	new_user = User(fname,lname,password)
	return new_user
