
import urllib, urllib2, cookielib, getpass, time
from bs4 import BeautifulSoup

def login():

	# Get username & password
	username = "underwater" #raw_input("Username: ")
	password = "!koolaidgirl" #getpass.getpass()

	# Set up CookieJar and opener
	cookie_jar = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]	# Unethical? ;)

	# This bit makes sense!
	login_url = "http://forum.austinimprov.com/ucp.php?mode=login"
	login_data = urllib.urlencode(
		{
			'username': 	username,
			'password': 	password,
			'autologin': 	'on', 
			'login':		'Login' 
		 })

	# Here we go!
	response = opener.open(login_url, login_data)

	# Go to the Control Panel page & get form_token, creation_time & birthday
	control_panel_url = "http://forum.austinimprov.com/ucp.php?i=173"
	response = opener.open(control_panel_url)
	html = BeautifulSoup(response.read())
	creation_time = html.find(attrs={"name":"creation_time"})['value']
	form_token = html.find(attrs={"name":"form_token"})['value']
	birthday = []
	for option in html.find_all('option', selected=True):
		birthday.append(option['value'])

	'''
	# Let's pretend I'm a human!
	time.sleep(1)

	# Now submit t3h form
	control_panel_url = "http://forum.austinimprov.com/ucp.php?i=profile&mode=profile_info"
	control_panel_data = urllib.urlencode({
		'aim': 			 'stillworkingyay',
		'submit': 		 'Submit',
		'bday_day':      birthday[0],	# Yes, these were required
		'bday_month':    birthday[1],
		'bday_year':     birthday[2],
		'form_token': 	 form_token,
		'creation_time': creation_time
	})

	# POST
	response = opener.open(control_panel_url, control_panel_data)
	'''
	return birthday
