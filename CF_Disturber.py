
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip as pc


def setup ( username, password ):
	dir = r"C:\Users\HP\Desktop\chromedriver_win32"
	chrome_driver_path = dir + "\chromedriver.exe"
	# options = webdriver.ChromeOptions ()
	# options.add_argument ('headless')
	driver = webdriver.Chrome (chrome_driver_path)  # options=options)
	driver.maximize_window ()
	url = "https://codeforces.com/enter"
	driver.get (url)
	handle = driver.find_element_by_id ("handleOrEmail")
	passw = driver.find_element_by_id ("password")
	handle.send_keys (username)
	passw.send_keys (password)
	checkbox=driver.find_element_by_id("remember")
	if(checkbox.is_selected()):
		pass
	else:
		checkbox.click()
	x = passw.submit ()
	driver.implicitly_wait (1000)
	time.sleep (2)
	return driver





def start ( ):

	Username = "indrajit1"
	Password = "aliveisawesome"
	driver = setup (Username, Password)
	want_to_disturb="its_aks_ulure"
	time_interval=60 #in seconds
	url = "https://codeforces.com/usertalk?other="+want_to_disturb
	message="Hello"

	while(True):
		driver.get (url)
		text_area = driver.find_elements_by_class_name ('wysiwyg')[2]
		driver.find_element_by_class_name ('html').click()
		pc.copy (message)
		text_area.send_keys (Keys.CONTROL+'v')
		driver.implicitly_wait (100)
		btn = driver.find_elements_by_class_name ("submit")[1]
		btn.submit ()
		driver.implicitly_wait (1000)
		time.sleep (time_interval)
start()