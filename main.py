from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from yaspin import yaspin, Spinner
import getpass

sp = Spinner(["😸", "😹", "😺", "😻", "😼", "😽", "😾", "😿", "🙀"], 200)

login = input("Enter fb email: ")
passw = getpass.getpass("Enter fb password: ")

browser = webdriver.Chrome()
browser.get('https://m.facebook.com/login.php')
email =  browser.find_element_by_id("m_login_email")
password = browser.find_element_by_id("m_login_password")
email.send_keys(login)
password.send_keys(passw, Keys.RETURN)

key = input("Search key: ")

import time
time.sleep(1)

browser.get(f'https://m.facebook.com/{key}/posts/')

with yaspin(sp, text="Okno chrome musi być aktywne, patrz na nie!!!"):
    for _ in range(120):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(.5)

        posts = browser.find_elements_by_class_name("_5rgt")
        for i in posts:
            if len(i) < 5:
                continue
            try:
                t = i.find_element_by_tag_name("p")
                with open("fake-posts.csv", 'a') as fp:
                    fp.write("\n---\n")
                    fp.write('\n'.join(i.text.split('\n')[:-1]))
            except:
                pass
        
        browser.execute_script("let posts = document.querySelectorAll('._3drp'); for (i of posts){ console.log(i); i.remove()}")
