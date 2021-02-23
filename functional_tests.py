from selenium import webdriver

broweser = webdriver.Firefox()
broweser.get('http://localhost:8000')

assert 'Django' in broweser.title