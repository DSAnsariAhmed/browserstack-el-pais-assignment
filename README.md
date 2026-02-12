# El País Opinion Scraper – Selenium + BrowserStack Assignment

## 📌 Project Overview

This project was developed as part of a technical assignment to demonstrate practical skills in:

- Web scraping using Selenium
- API integration
- Text processing
- Image downloading
- Cross-browser testing using BrowserStack
- Parallel execution

The script visits the Spanish news website **El País**, extracts data from the Opinion section, translates article titles into English using an API, performs text analysis, and validates functionality across multiple browsers and devices using BrowserStack.

This repository contains the complete end-to-end implementation of the assignment.

---

## 🎯 Assignment Objectives Covered

The following requirements were implemented exactly as specified:

1. Visit El País website
2. Ensure content is displayed in Spanish
3. Scrape first 5 articles from the Opinion section
4. Print article titles and content in Spanish
5. Download and save cover images locally
6. Translate article titles into English using an API
7. Perform text analysis on translated titles
8. Run the solution locally to verify functionality
9. Execute cross-browser testing using BrowserStack across 5 parallel threads on desktop and mobile environments

---

## 🛠️ Technologies Used

- Python
- Selenium WebDriver
- Requests library
- RapidAPI (Rapid Translate Multi Traduction API)
- BrowserStack Automate
- Threading (Parallel Execution)

---

## 📂 Project Structure

browserstack-el-pais-assignment/<br>
│<br>
├── main.py # Scraping + translation + text analysis <br>
├── Browserstack_test.py # Cross-browser execution script <br>
├── requirements.txt # Python dependencies <br>
├── README.md # Project documentation <br>
└── images/ # Downloaded article images <br>
├── article_1.jpg<br>
├── article_2.jpg<br>
├── article_3.jpg<br>
├── article_4.jpg<br>
└── article_5.jpg<br>

---

## ⚙️ Implementation Details (Step-by-Step)

### 1️⃣ Website Navigation

- Opened the El País Opinion section:
- The website content is naturally displayed in Spanish by default.
- Selenium was used to interact with the webpage and extract dynamic content.

---

### 2️⃣ Web Scraping Using Selenium

From the Opinion section:

- Located the first 5 articles
- Extracted:
- Article titles (Spanish)
- Article links

For each article:
- Opened the article page
- Extracted content paragraph-by-paragraph
- Printed the content in Spanish

---

### 3️⃣ Image Download

For each article:

- Located the first available image element
- Extracted the image URL
- Downloaded using the `requests` library
- Saved locally
- The website content is naturally displayed in Spanish by default.
- Selenium was used to interact with the webpage and extract dynamic content.

---

### 4️⃣ Translation API Integration

Used:
- RapidAPI – Rapid Translate Multi Traduction API

Process:
- Collected all Spanish article titles
- Sent translation request:
  - Source language: Spanish (es)
  - Target language: English (en)
- Received translated titles
- Printed results

Example:
Spanish: Exceso de ruido
English: Excess noise

---

### 5️⃣ Text Processing

From the translated titles:

- Split titles into words
- Normalized text:
  - Converted to lowercase
  - Removed punctuation
- Counted frequency of each word
- Printed words repeated more than twice

Example output:
No words repeated more than twice.

---

### 6️⃣ Local Execution

Before cloud testing, the script was fully verified locally to ensure:

- Scraping worked correctly
- Images saved properly
- Translation API responded correctly
- Output formatting was clean and readable

---

### 7️⃣ Cross-Browser Testing (BrowserStack)

A separate script (`Browserstack_test.py`) was created to run tests on BrowserStack.

Key features:

- 5 parallel threads
- Desktop + Mobile testing environments:

  - Chrome – Windows 11
  - Firefox – Windows 10
  - Edge – Windows 11
  - Safari – macOS Sonoma
  - iPhone 14 – Mobile (iOS)

Each session:
- Opened El País
- Verified page load
- Executed remotely on real devices/browsers

---

## 🚧 Challenges Faced & How They Were Solved

This assignment involved multiple real-world issues which were debugged and resolved step-by-step.

### 🔹 Challenge 1: ChromeDriver Version Mismatch
**Issue:**
ChromeDriver was incompatible with the installed Chrome browser version.

**Solution:**
- Manually downloaded the matching ChromeDriver version
- Linked it correctly with Selenium

---

### 🔹 Challenge 2: Dynamic Website Structure
**Issue:**
Some articles had different layouts.
Some content sections were shorter or missing.

**Solution:**
- Used flexible paragraph extraction
- Added conditions to ignore empty or very short text
- Handled layout variations gracefully

---

### 🔹 Challenge 3: Image Download Problems
**Issue:**
Some downloaded images were not viewable.

**Cause:**
Incorrect image source selection.

**Solution:**
- Filtered valid image URLs
- Selected JPG/JPEG sources carefully

---

### 🔹 Challenge 4: Translation API Errors
**Issue:**
Initial API responses were incorrect.

**Cause:**
Wrong language codes and payload formatting.

**Solution:**
- Corrected language settings:

from: "es"
to: "en"

- Fixed request payload structure

---

### 🔹 Challenge 5: Selenium 4 Compatibility Issue
**Issue:**
Error occurred:

desired_capabilities not supported


**Solution:**
- Updated code to use:
options.set_capability()


---

### 🔹 Challenge 6: BrowserStack Parallel Execution
**Issue:**
Understanding how to:
- Connect Selenium to BrowserStack cloud
- Run multiple sessions simultaneously

**Solution:**
- Used Python threading
- Created separate configurations for:
- Desktop browsers
- Mobile device
- Verified execution through BrowserStack dashboard

---

### 🔹 Challenge 7: Security Concern
**Issue:**
BrowserStack credentials were visible in code.

**Solution:**
- Replaced credentials with placeholders before uploading to GitHub

---

## 📊 Results Achieved

Successfully demonstrated:

- Real-time web scraping
- API integration
- Text processing
- Image handling
- Cloud-based cross-browser testing
- Parallel execution
- Debugging and problem-solving

---


---

## 🔐 Security Note

BrowserStack credentials are intentionally not included in this repository.

Replace the placeholders in the script with your own credentials before running.

---

## 📎 Final Outcome

This project successfully demonstrates:

- Web automation
- API integration
- Text analysis
- Cloud-based testing
- Cross-browser validation
- Real-world debugging and troubleshooting

All assignment requirements were fully implemented and verified.
