from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import pyautogui

path = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
hashtags = ["#programming", "#coding", "#programmer", "#python", "#java","#programmingmemes", "#programminghumor",'#computerscience', '#html', '#webdeveloper','#tech', '#software', '#codinglife', '#webdevelopment','#css','#linux', '#programmers', '#programmingmemes', '#softwaredeveloper','#programminglife','#webdesign']
commentlist = []

def login():
    driver.get("https://www.instagram.com/")
    driver.maximize_window()

    time.sleep(3)
    driver.find_element_by_xpath("//input[@name=\'username\']").send_keys("coders.arena_")
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys("aditya@123")
    driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

    time.sleep(3)

def search():
    input = random.choice(hashtags)
    search = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/input")
    search.send_keys(input)

    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]").click()
    time.sleep(2)
    driver.refresh()
    time.sleep(3)
    find = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[1]/div/div/div[1]/div[1]")
    find.click()

def hashtag():
    hashtag_list = []
    hashtag_count = 1

    hashtag_list.clear()
    hashtag_count = 0
    gethashtags = driver.find_elements_by_class_name("xil3i")
    for tag in gethashtags:
        hashtag_list.append(tag.get_attribute("text"))

    for tag in hashtag_list:
        if tag in hashtags:
            hashtag_count += 1
    
    return hashtag_count

def getposts():
    limits = [1000, 50, 20]
    limit_count = [0, 0, 0]
    like_limit = True
    cmt_limit = True
    flw_limit = True
    time.sleep(2)

    count1 = 0
    count2 = 0
    while count1 < 150:
        time.sleep(3)
        if count2 <= 20:  
            hashtag_count = hashtag()  
            time.sleep(3)
            if(hashtag_count >= 0 and like_limit == True):
                like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span")
                like.click()
                limit_count[0] += 1
                if limit_count[0] > limits[0]:
                    like_limit = False

            pyautogui.press("down")
            time.sleep(1)

            if(hashtag_count >= 7 and cmt_limit == True):
                commentlist = ["nice"]
                try:
                    comment_box = driver.find_element_by_class_name("Ypffh")
                    comment_box.click()
                    for i in random.choice(commentlist):
                        pyautogui.press(i)
                    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div[1]/form/button").click()
                    limit_count[1] += 1
                    if limit_count[1] > limits[1]:
                        cmt_limit = False
                except:
                    time.sleep(1)

            pyautogui.press('up')
            time.sleep(1)

            if(hashtag_count >= 10 and flw_limit == True):
                follow = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
                following = follow.get_attribute("text")
                print(following)
                if following=="Follow":
                    follow.click()
                    limit_count[2] += 1
                    if limit_count[2] > limits[2]:
                        flw_limit = False
            time.sleep(1)

            count2 += 1
            time.sleep(2)
            driver.find_element_by_link_text("Next").click()
            time.sleep(1)
        else:
            count2 = 0
            pyautogui.press('up')
            time.sleep(1)
            close = driver.find_element_by_xpath("/html/body/div[4]/div[3]/button/div")
            close.click()
            time.sleep(1)
            search()
            time.sleep(2)    
        count1 += 1 

if __name__ == '__main__':
    login()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)
    search()
    time.sleep(2)
    getposts()