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
    notNow = driver.find_element_by_xpath('''/html/body/div[4]/div/div/div/div[3]/button[2]''')
    notNow.click()

    driver.get(profileName)
    sleep(6)
    following = driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a''')
    following.click()
    sleep(4)
    buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Seguindo')]")
    i = 0
    while len(buttons) > 1:
        try:
            buttons[i].click()
        except:
            pass
        unfollowBtns = driver.find_elements_by_xpath("//*[contains(text(), 'Deixar de seguir')]")
        try:
            unfollowBtns[1].click()
            sleep(1)
        except:
            pass

        i = i + 1
        #do again
        if i > 5:
            i = 0
            buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Seguindo')]")
