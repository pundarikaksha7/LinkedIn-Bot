from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/yourusername/chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(2)

#********** LOG IN *************

username = driver.find_element("xpath","//input[@name='session_key']")
password = driver.find_element("xpath","//input[@name='session_password']")

username.send_keys('youremail')
password.send_keys('yourpassword')
time.sleep(2)

submit = driver.find_element("xpath","//button[@type='submit']").click()

driver.get("linkedin profile link in search bar")
time.sleep(2)

#***************** Send Request *********

all_buttons = driver.find_elements(By.TAG_NAME, "button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
 	driver.execute_script("arguments[0].click();", btn)
 	time.sleep(2)
 	# other=driver.find_element(By.XPATH,"//button[@aria-label='Other']")
 	# driver.execute_script("arguments[0].click()",other)
 	
 	# time.sleep(2)
 	addnote=driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
 	driver.execute_script("arguments[0].click();", addnote)
 	text_area = driver.find_element(By.ID,'custom-message')
 	text_area.send_keys("Greetings, I am an organizer at Techniche, the annual techno-management festival of IIT Guwahati. It is the largest of its kind in north-eastern India and one of the largest tech fests of the country.I am hoping to connect and associate with you for the same. Can I get your contact number and email?")
 	time.sleep(2)
 	send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
 	driver.execute_script("arguments[0].click();", send)
 	time.sleep(2)