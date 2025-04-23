# 🏠 Zillow Property Scraper & Google Form Filler

This project demonstrates a complete end-to-end automation pipeline built with **Python**, combining **web scraping** and **form submission automation**.

It scrapes property listings (address, price, link) from a Zillow-like website, then uses **Selenium** to automatically submit this data into a **Google Form** — mimicking a data-entry task often performed by hand.

## 🔧 Tools & Libraries Used
- `requests` + `BeautifulSoup` for static HTML scraping
- `Selenium` for browser automation
- `dotenv` for secure form URL handling
- `ChromeDriver` for automation

## 📦 Features
- Extracts property **price**, **address**, and **URL**
- Cleans and stores results in memory
- Submits form data using an automated Chrome browser
- Works with minimal setup and can be extended for CSV export or database storage

## 🚀 How to Run

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   
2. Set up a .env file:
```
GOOGLE_FORM=https://your-google-form-url-here
```
3. Run the script:
```bash 
python main.py
```

⚠️ Ensure ChromeDriver is installed and matches your local Chrome version.
