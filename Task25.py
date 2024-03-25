from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class IMDB:
    """
        This class is used to search IMDB website
    """

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #self.wait = WebDriverWait(self.driver, 20)

        self.wait = WebDriverWait(self.driver, 30, poll_frequency=3)

        self.action = ActionChains(self.driver)

    def boot(self):
        """
               This method is used to open browser and go to  website
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait.until(ec.url_to_be(self.url))

    def quit(self):
        self.driver.quit()

    def fillForm(self):
        """
        This method is used to fill the search form and click on See result button
        """
        # Open Name Menu
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='nameTextAccordion']"))).click()
        #Enter Name
        self.wait.until(ec.presence_of_element_located((By.XPATH, "// input[contains( @ name, 'name-text-input')]"))).send_keys("Robert")

        # Open BirthDate Menu
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='birthDateAccordion']"))).click()
        # Enter start year and End year
        self.wait.until(ec.presence_of_element_located((By.XPATH, "// input[contains( @ name, 'birth-year-month-start-input')]"))).send_keys("2000")
        self.wait.until(ec.presence_of_element_located((By.XPATH, "// input[contains( @ name, 'birth-year-month-end-input')]"))).send_keys("2023")

        # Open Birthday Menu
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='birthdayAccordion']"))).click()
        #Enter Birthday
        self.wait.until(ec.presence_of_element_located((By.XPATH, "// input[contains( @name,'birthday-input')]"))).send_keys("04-04")

        # Open Awards and Recognition Menu
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='awardsAccordion']/div[1]/label/span[2]"))).click()
        # Select Best Actor Nominated
        self.wait.until(ec.presence_of_element_located((By.XPATH, "// *[ @id='accordion-item-awardsAccordion']/div/section/button[2]"))).click()

        # Open Page Topics  Menu
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='pageTopicsAccordion']"))).click()
        #Select Award Nominations Option
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='accordion-item-pageTopicsAccordion']/div/div/section/button[1]"))).click()


        # Open Gender  Menu
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='genderIdentityAccordion']"))).click()
        #Select Award Nominations Option
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='accordion-item-genderIdentityAccordion']/div/section/button[1]"))).click()

        # Open Gender  Menu
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='adultNamesAccordion']"))).click()
        # Select Award Nominations Option
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='include-adult-names']"))).click()


        # Click on See Result button
        self.wait.until(ec.presence_of_element_located((By.XPATH, "// button[contains( @class,'ipc-btn')][1]"))).click()


obj = IMDB("https://www.imdb.com/search/name/")
obj.boot()
obj.fillForm()
obj.quit()









