from selenium import webdriver as driver
from selenium.webdriver.common.keys import Keys

class Pages():
    GOOGLE = "https://www.google.com"
    GOOGLE_PICS = "https://www.google.cz/imghp"
    GOOGLE_SEARCH_BAR = "//*[@id=\"tsf\"]/div[2]/div[1]/div[1]/div/div[2]/input"
    GOOGLE_QUERY = "https://google.com/search?q="
    GOOGLE_PICS_QUERY = "https://www.google.cz/imghp?q="
    YOUTUBE_QUERY = "https://www.youtube.com/results?search_query="

class Web:
    def __init__(self):
        self.browser = driver.Chrome(executable_path="C:\Program Files (x86)/chromedriver.exe")

    def searchForPhrase(self, phrase):
        self.browser.get(str(Pages.GOOGLE_QUERY) + phrase)

    def searchForWord(self, word):
        self.browser.get(Pages.GOOGLE)
        element = self.browser.find_element_by_xpath(Pages.GOOGLE_SEARCH_BAR)
        element.send_keys(word)
        element.send_keys(Keys.ENTER)

    def searchYoutube(self, phrase):
        self.browser.get(str(Pages.YOUTUBE_QUERY) + phrase)
        
    def showImages(self, image):
        self.browser.get(str(Pages.GOOGLE_PICS_QUERY) + image)
        element = self.browser.find_element_by_xpath("/html/body/div/div[3]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
        element.send_keys(Keys.ENTER)
