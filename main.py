from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from yaspin import yaspin, Spinner
import csv

sp = Spinner(["😸", "😹", "😺", "😻", "😼", "😽", "😾", "😿", "🙀"], 200)

browser = webdriver.Chrome()
browser.get('https://m.facebook.com/login.php')
email =  browser.find_element_by_id("m_login_email")
password = browser.find_element_by_id("m_login_password")
login = input("Enter fb email: ")
email.send_keys(login)
passw = input("Enter fb password: ")
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
        posts_text = []
        for i in posts:
            try:
                t = i.find_element_by_tag_name("p")
                posts_text.append(i.text)
            except:
                pass
        with open("fake-posts.csv", 'a') as fp:
            spamwriter = csv.writer(fp, delimiter=',')
            spamwriter.writerow([x[:-16] for x in posts_text])
        browser.execute_script("let posts = document.querySelectorAll('._3drp'); for (i of posts){ console.log(i); i.remove()}")
