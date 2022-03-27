from selenium import webdriver
import time

driver = webdriver.Edge(executable_path = 'C:\\Users\\steve\\Downloads\\edgedriver_win64\\msedgedriver.exe')

driver.get('https://twitter.com/login')

email = 'steven.e.eno@gmail.com'
password = ''