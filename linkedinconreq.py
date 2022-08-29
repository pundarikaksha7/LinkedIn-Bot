from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/YourUserName/chromedriver.exe') #insert the location of your driver.exe here
driver.get('https://www.linkedin.com')
time.sleep(2)

#********** LOG IN *************

username = driver.find_element("xpath","//input[@name='session_key']")
password = driver.find_element("xpath","//input[@name='session_password']")

username.send_keys('youremailid') #insert your email address to Log into LinkedIn here
password.send_keys('yourpassword') #enter your password here
time.sleep(2)

submit = driver.find_element("xpath","//button[@type='submit']").click()

#enter the links of all the LinkedIn ids you want to send a note to
LINKEDIN_LINKS=[
"https://www.linkedin.com/in/pundarikaksha7/"

]

for i in LINKEDIN_LINKS:
	driver.get(i)
	time.sleep(2)

#**********SEND REQUEST **********

	all_buttons = driver.find_elements(By.TAG_NAME, "button")
	connect_buttons = [btn for btn in all_buttons if btn.text == "Connect" or btn.text=="Follow" or btn.text=="Pending"]



	# for btn in connect_buttons:
	btn=connect_buttons[0];
	if btn.text=="Connect":
		driver.execute_script("arguments[0].click();", btn)
		time.sleep(2)
			 	
		addnote=driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
		driver.execute_script("arguments[0].click();", addnote)
		text_area = driver.find_element(By.ID,'custom-message')

		#Enter your text inside the send keys function here
		text_area.send_keys("Your message")
		time.sleep(2)
		send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
		driver.execute_script("arguments[0].click();", send)
		time.sleep(2)

	elif btn.text=="Follow" or btn.text=="Pending":
		btn2=driver.find_elements(By.XPATH,"//button[@aria-label='More actions']")
		driver.execute_script("arguments[0].click();", btn2[1])
		time.sleep(2)
		driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[3]/div/div/ul/li[4]/div").click()
		
		connectagain=driver.find_element(By.XPATH,"//button[@aria-label='Connect']")
		driver.execute_script("arguments[0].click();",connectagain)
		

		
		addnote=driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
		driver.execute_script("arguments[0].click();", addnote)
		text_area = driver.find_element(By.ID,'custom-message')

		#Enter your text inside the send keys function here

		text_area.send_keys("Your message")
		time.sleep(2)
		send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
		driver.execute_script("arguments[0].click();", send)
		time.sleep(5)
		continue
