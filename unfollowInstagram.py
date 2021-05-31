from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def unfolowAllInsta(link, profileName, emailOrNumber, pwd):
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(link)
    sleep(3)
    enterFB = driver.find_element_by_xpath('''//*[@id="loginForm"]/div/div[5]/button/span[2]''')
    enterFB.click()

    email = driver.find_element_by_xpath('''//*[@id="email"]''')
    email.send_keys(emailOrNumber)

    passw = driver.find_element_by_xpath('''// *[ @ id = "pass"]''')
    passw.send_keys(pwd)

    loginButton = driver.find_element_by_xpath('''// *[ @ id = "loginbutton"]''')
    loginButton.click()
    sleep(7)
    try:
        notNow = driver.find_element_by_xpath('''/html/body/div[4]/div/div/div/div[3]/button[2]''')
        notNow.click()
    except:
        pass

    while True:
        driver.get(profileName)
        sleep(4)
        following = driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a''')
        following.click()
        sleep(4)
        people = driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")

        if len(people) <= 0:
            break

        followingLinks = []
        for p in people:
            followingLinks.append('https://www.instagram.com/' + p.text)

        for link in followingLinks:
            try:
                driver.get(link)
                driver.find_element_by_xpath(
                    '''//*[@id="react-root"]/section/main/div/header/section/div[2]''').get_attribute('innerHTML')
                sleep(1)
                try:
                    btnFriend = driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[2]/div/span/span[1]/button/div/span""")
                except:
                    btnFriend = driver.find_element_by_xpath(
                        """//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button""")

                btnFriend.click()

                unfollowBtn = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
                unfollowBtn.click()
            except:
                pass


