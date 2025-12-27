# TenForce Automation Project

## This repository contains a Selenium-based automation suite for the TenForce Career page navigation.

##  How to Run
1. **Install requirements:** `pip install -r requirements.txt`
2. **Execute tests:** `pytest`
3. **View Results:** An HTML report will be generated in the `reports/` folder. 

##  Architecture (POM)
I implemented the **Page Object Model (POM)** to keep the test steps separate from the website's technical details.
* **BasePage:** The "engine" that handles scrolling and smart-clicking.
* **CareerPage:** The "map" containing the specific TenForce locators.



##  Why I made these choices

### Solving the "Sticky Header"
TenForce has a menu that stays at the top of the screen. Standard clicks often failed because the menu "blocked" the buttons. I solved this by creating a **Scroll-to-Center** function. This uses JavaScript to move the element to the middle of the screen before clicking, so the header never gets in the way.

### Robust Locators
Instead of using fragile XPaths like `/div/div/h3`, I used **Text-Based Locators** with `normalize-space()`. This ensures the test is "smart" enough to find the "Life of two interns" article even if the website's code changes slightly. 

### Meaningful Assertions
I didn't just check if the page loaded; I verified the specific text node for the CV submission instructions. This proves the Career section is actually working, not just visible. 
