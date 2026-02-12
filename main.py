from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
from collections import Counter
import re

# TRANSLATION FUNCTION
def translate_text(text):
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

    payload = {
        "from": "es",
        "to": "en",
        "q": [text]
    }
    headers = {
        "x-rapidapi-key": "128fad34e6msh8c3dd09d5e13a12p101d95jsnb8a085b657ec",
        "x-rapidapi-host": "rapid-translate-multi-traduction.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        result = response.json()
        return result[0]
    except:
        return "Translation Error"


# SELENIUM SETUP 
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Opinion page
driver.get("https://elpais.com/opinion/")
time.sleep(7)

articles = driver.find_elements(By.CSS_SELECTOR, "article")

titles = []
links = []

# STEP 1: GET FIRST 5 TITLES + LINKS 
for article in articles:
    try:
        title = article.find_element(By.TAG_NAME, "h2").text
        link = article.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")

        if title.strip() == "":
            continue

        titles.append(title)
        links.append(link)

        if len(titles) == 5:
            break

    except:
        continue


# STEP 2: VISIT EACH ARTICLE
print("\n=========== STEP 1 & 2: SCRAPED ARTICLES (SPANISH) ===========\n")

for i in range(5):
    print("\n======================\n")
    print(f"Article {i+1}")
    print("Spanish Title:", titles[i])

    driver.get(links[i])
    time.sleep(5)

    print("\nContent:\n")

    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    found = False

    for p in paragraphs:
        text = p.text.strip()
        if len(text) > 40:
            print(text)
            found = True

    if not found:
        print("Content not available or different layout.")

    # SAVE COVER IMAGE
    try:
        images = driver.find_elements(By.TAG_NAME, "img")

        for image in images:
            img_url = image.get_attribute("src")

            if img_url and ("jpg" in img_url or "jpeg" in img_url):
                img_data = requests.get(img_url).content

                with open(f"images/article_{i+1}.jpg", "wb") as f:
                    f.write(img_data)

                print("\nImage saved as:", f"article_{i+1}.jpg")
                break

    except:
        print("\nNo image found")


# STEP 3: TRANSLATE TITLES
print("\n\n=========== TRANSLATED HEADERS ===========\n")

translated_titles = []

for i, title in enumerate(titles):
    try:
        english_title = translate_text(title)
        translated_titles.append(english_title)

        print(f"Article {i+1}")
        print("Spanish :", title)
        print("English :", english_title)
        print()

    except:
        print(f"Translation failed for: {title}")

driver.quit()

print("\n=========== WORD FREQUENCY ANALYSIS ===========\n")

all_words = []

for title in translated_titles:
    words = re.findall(r'\b[a-zA-Z]+\b', title.lower())
    all_words.extend(words)

word_counts = Counter(all_words)

found = False
for word, count in word_counts.items():
    if count > 2:
        print(f"{word} → {count} times")
        found = True

if not found:
    print("No words repeated more than twice.")