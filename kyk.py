from kyk_adina import username, password
from selenium import webdriver

url = "https://wifi.gsb.gov.tr/login.html"


# ÖNCE GİRİŞİ SAĞLIYORUZ
def logIn(username, password):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[1]/td[2]/input").send_keys(username)
    browser.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[2]/td[2]/input").send_keys(password)
    browser.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[3]/td/input").click()
    


logIn(username,password)
