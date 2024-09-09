from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()

driver.get('https://faculty.uca.edu/vparuchuri/4315/4315_quiz1.htm')

name_element = driver.find_element("name", "student_name")
name_element.send_keys('script test')

Q1 = driver.find_element("name", "TF:1")
Q1select = Select(Q1)
Q1select.select_by_value("T")

Q2 = driver.find_element("name", "TF:2")
Q2select = Select(Q2)
Q2select.select_by_value("F")

Q3 = driver.find_element("name", "MC:3")
Q3select = Select(Q3)
Q3select.select_by_value("D")

Q4 = driver.find_element("name", "MC:4")
Q4select = Select(Q4)
Q4select.select_by_value("B")

Q5 = driver.find_element("name", "MC:5")
Q5select = Select(Q5)
Q5select.select_by_value("C")

Q6 = driver.find_element("name", "MC:6")
Q6select = Select(Q6)
Q6select.select_by_value("D")

Q7 = driver.find_element("name", "MC:7")
Q7select = Select(Q7)
Q7select.select_by_value("B")

Q8 = driver.find_element("name", "MC:8")
Q8select = Select(Q8)
Q8select.select_by_value("F")

Q9 = driver.find_element("name", "MC:9")
Q9select = Select(Q9)
Q9select.select_by_value("A")

Q10 = driver.find_element("name", "MC:10")
Q10select = Select(Q10)
Q10select.select_by_value("D")

ID_element = driver.find_element("name", "student_id")
ID_element.send_keys("B01278750")

email_element = driver.find_element("name", "student_email")
email_element.send_keys("aharris47@cub.uca.edu")

submit_element = driver.find_element("xpath", "//input[@src='4315_quiz1_files/submit.gif']")
submit_element.click()

time.sleep(3)

send_element = driver.find_element("id","proceed-button")
send_element.click()

driver.quit()


