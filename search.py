from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://youtube.com")   #site to open

searchbox= driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys("hello")    #what to search for

enter_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
enter_button.click()        #"click" search