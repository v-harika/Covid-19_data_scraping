from selenium import webdriver
import re
import smtplib

class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Users/namosri/Downloads/chromedriver_win32/chromedriver.exe")
    def get_data(self):
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(., 'India')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        total_cases = data[2]
        new_cases = data[3]
        total_deaths = data[4]
        new_deaths = data[5]
        total_recovered = data[6]
        active_cases = data[7]
        serious_critical = data[8]

        send_mail(country_element.text, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical)

        self.driver.close()
        self.driver.quit()
def send_mail(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender@gmail.com', 'password')

    subject = 'Coronavirus status in your country today!'

    body = 'Today in ' + country_element + '\
        \nThere is new data on coronavirus:\
        \nTotal cases: ' + total_cases +'\
        \nNew cases: ' + new_cases + '\
        \nTotal deaths: ' + total_deaths + '\
        \nNew deaths: ' + new_deaths + '\
        \nActive cases: ' + active_cases + '\
        \nTotal recovered: ' + total_recovered + '\
        \nSerious, critical cases: ' + serious_critical  + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('receiver@gmail.com','sender@gmail.com',msg)
    print('Hey Email has been sent!')

    server.quit()
bot = Coronavirus()
bot.get_data()
