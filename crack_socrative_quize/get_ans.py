from selenium.webdriver import Firefox
import json
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4 as bs


url = input("Enter the URL : ")

driver = Firefox(executable_path="G:/software/geckodriver/geckodriver.exe")
driver.get("https://b.socrative.com/login/teacher/")
delay = 3
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'teacherLoginForm')))
    driver.find_element_by_name("email").send_keys("sd@inbox-me.top")

    driver.find_element_by_name("password").send_keys("1234567890")

    btn = driver.find_element_by_id("teacherLoginButton")
    btn.click()
    
    time.sleep(15)
    
    driver.get(url)

    _js = driver.page_source

    get_div = bs.BeautifulSoup(_js, 'html.parser')

    final_js = json.loads(get_div.find("div", id="json").text)

    with open("Final_json.json", "w") as f:
        f.write(json.dumps(final_js, indent=4))

    final_dict = {}
    count = 0

    with open("Final_json.json", "r") as f:
        data = json.loads(f.read())

    for q in data['questions']:
        count += 1
        final_dict[count] = {
            "Question is : ": q['question_text'],
        }

        for a in q['answers']:
            if a['is_correct'] is True:
                final_dict[count].update({"Answer : ": a['text']})

    with open("final_ans.txt", "w") as f:
        for k, v in final_dict.items():
            f.write(f"{k} {v['Question is : ']} \n ==> {v['Answer : ']}\n\n")

except Exception as e:
    pass


# driver.find_element_by_xpath("//input[name()='email']").send_keys("sd@inbox-me.top")
#
# driver.find_element_by_xpath("//input[name()='password']").send_keys("1234567890")
#
# btn = driver.find_element_by_id("teacherLoginButton")
# btn.click()
#
# driver.switch_to.window(driver.window_handles[1])
# driver.get(url)
#
# text = driver.find_element_by_id("pre")
#
# _js = text.text
#
# final_js = json.loads(_js)
#
# print(final_js)
