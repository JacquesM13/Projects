import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSd1V-z_NIdsaz0MqKB3-8xcc_4qLGX52_d_Q4sL7HxfkhsEIg/viewform?usp=dialog'
ZILLOW_PAGE = 'https://appbrewery.github.io/Zillow-Clone/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options= chrome_options)

driver.get(url= GOOGLE_FORM_LINK)

response = requests.get(url= ZILLOW_PAGE)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

prices = soup.select(selector= 'span[data-test="property-card-price"]')
# print(prices)

addresses = soup.select(selector= 'address[data-test="property-card-addr"]')

links = soup.select(selector= 'a.property-card-link')

address_list = []
for address in addresses:
    address_list.append(address.text.strip())

price_list = []
for price in prices:
    price_list.append(price.text.split()[0].split('+')[0].split('/mo')[0])

property_links = []
for link in links:
    property_links.append(link['href'])
    print(link['href'])

print(price_list)
print(address_list)
print(property_links)

properties_dict = {addr: (p, l) for addr, p, l in zip(address_list, price_list, property_links)}
print(properties_dict)

for key, values in properties_dict.items():
    input_fields = driver.find_elements(By.CSS_SELECTOR, value='input[type="text"]')
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    print(f"Key: {key}, values: {values}")
    input_fields[0].send_keys(key)
    input_fields[1].send_keys(values[0])
    input_fields[2].send_keys(values[1])
    sleep(2)
    submit_button.click()
    sleep(2)
    submit_another_response = driver.find_element(By.XPATH, "//a[text()='Submit another response']")
    submit_another_response.click()
    sleep(2)
    
driver.quit()
