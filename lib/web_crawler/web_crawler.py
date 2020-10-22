from selenium import webdriver

class create_acc():

    def __init__(self):
        self.set_up()
        self.start_website()

    def set_up(self):
            self.driver = webdriver.Chrome('../webdriver/chromedriver.exe')

    def start_website(self):
        self.driver.get('https://en.titolo.ch/')

    def create_acc(self):
        pass