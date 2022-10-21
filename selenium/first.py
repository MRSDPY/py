from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

with Firefox(executable_path='G:/software/geckodriver/geckodriver.exe') as driver:
	driver.get("https://www.google.com")
	data = "game-leader.herokuapp.com"
	search = driver.find_element_by_css_selector(".gLFyf")
	search.send_keys(data)
	search.submit()

	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div/h3/a")))



