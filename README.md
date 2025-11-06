Juspay Automation Challenge — Selenium | Python | Firefox

This project demonstrates automation of a real payment journey using
✅ Selenium WebDriver
✅ Python
✅ Firefox (GeckoDriver)
✅ WebDriver-Manager

As required in the Juspay Automation Challenge, this script automates:

✅ Login to Amazon
✅ Searching a product
✅ Selecting first product
✅ Adding to Cart
✅ Proceeding to Checkout
✅ Navigating until OTP page (if displayed)

✅ 1. Features Automated

Opens Amazon.in

Logs in using user credentials

Searches for "Headphones" (can be modified)

Selects first search result

Opens product page

Adds item to cart

Opens cart

Proceeds to checkout

Reaches payment selection page / OTP prompt

This demonstrates a complete e-commerce payment workflow.

2. Technology Stack
Component	Technology
Language	Python 3.x
Automation	Selenium WebDriver
Browser	Firefox
Driver Handling	WebDriver Manager
Test Execution	Python Script

3. Project Structure
juspay0611/
│
├── automation_script.py      # Main automation script
├── README.md                 # Documentation
├── requirements.txt          # Dependencies
└── recordings/               # Video recording (optional)
✅ 4. Installation Instructions

Step 1 — Clone the repository
git clone https://github.com/kalyanBrahmam0805/juspay0611.git
cd juspay0611

✅ Step 2 — Create virtual environment
Windows
python -m venv venv
venv\Scripts\activate

Mac / Linux

python3 -m venv venv
source venv/bin/activate

✅ 5. How to Run The Automation
python automation_script.py

✅ 6. Video Recording (Required for Juspay Task)

You must record the automation using any screen recorder:

✅ Windows — Win + G (Xbox Game Bar)
✅ OBS Studio
✅ Mac — QuickTime

✅ 7. Run on Any New System

This project is fully portable because:

✅ webdriver-manager auto-installs drivers
✅ No manual setup needed
✅ Works anywhere Python is available

✅ 9. Contact

For support, reach out via GitHub:

👉 kalyanBrahmam0805