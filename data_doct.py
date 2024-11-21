from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json

# Set up Selenium WebDriver using Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.medindia.net/doctor-appointment/tele-consultation.asp?category=Allopathy%20Doctors")

time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'html.parser')

doctors = []

names = soup.find_all('h4', attrs={"class": "doc-name"})
specialties = soup.find_all('p', attrs={"class": "doc-speciality"})

for name, specialty in zip(names, specialties):
    doctor_info = {
        "name": name.text.strip(),
        "specialty": specialty.text.strip()
    }
    doctors.append(doctor_info)

with open('doctors_data.json', 'w', encoding='utf-8') as f:
    json.dump(doctors, f, ensure_ascii=False, indent=4)

driver.quit()

print(f"Data scraped and saved to doctors_data.json with {len(doctors)} records.")
