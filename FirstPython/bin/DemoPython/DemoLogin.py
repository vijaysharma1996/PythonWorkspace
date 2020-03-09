'''
Created on 05-Oct-2018

@author: mvelayutham
'''
from selenium import webdriver
driver = webdriver.Chrome(r'''C:\Users\mvelayutham\AppData\Local\Programs\Python\Python37\Scripts\chromedriver.exe''')
driver.get("http://qaft.operativeone.com")
driver.implicitly_wait(1000)
elem = driver.find_element_by_id("idToken1")
elem.send_keys("supportops@qaftautomation.com").keys().enter()
elem1 = driver.find_element_by_id("idToken2")
elem1.keys().enter()
elem1.send_keys("Oper@t1ve")
elem2 = driver.find_element_by_link_text("LOGIN").keys().enter()
driver.close()
