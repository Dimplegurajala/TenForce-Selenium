# TenForce QA Automation Project - Selenium

This repository contains a professional Selenium-based automation suite for the TenForce Career page user journey. The project is designed to be resilient, scalable, and easy to maintain.

# How to Run the Test

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

2.**Run the Test:**
Execute the following command to run the suite and generate an HTML report:
    pytest


## Architecture (Page Object Model)
​I implemented a strict Page Object Model (POM) to separate the test logic from the technical implementation details.

### BasePage:
Acts as the framework engine, containing generic, reusable actions like smart-clicking and specialized scrolling.

### CareerPage:
Serves as the object "map," holding the specific XPaths and business logic for the TenForce website.
​This separation ensures that if the website UI changes, updates are only required in the Page Object, keeping the test scripts clean and readable.

### Engineering Decisions (The "Why")

**​1. Solving the "Sticky Header" Interference**
​The TenForce website uses a floating navigation menu that stays at the top of the screen. Standard Selenium click() actions often failed because the menu physically "covered" the target elements.

​Solution: I implemented a JavaScript-based Scroll-to-Center function. This ensures the element is moved to the vertical center of the viewport before any interaction, guaranteeing the header never blocks the click.

**​2. Robust & Resilient Locators**
​To avoid "brittle" tests that break with minor UI changes, I avoided long, absolute XPaths (e.g., /div/div/h3).

​Solution: I utilized Text-Based Locators combined with normalize-space(). This makes the suite "smart" enough to find elements like the "Life of two interns" article even if the underlying HTML structure changes slightly.

**​3. Meaningful Assertions**
​I chose not to rely on simple URL checks, which can provide "false positives."

​Solution: The suite performs a deep validation by looking for the specific CV submission text node. This confirms that the Job Openings section is not just visible, but fully functional and displaying the correct contact data.

​**4. CI/CD Integration**
​The project is fully integrated with GitHub Actions. Every push to the repository triggers an automated run in a headless Linux environment, ensuring the code is "Green" and production-ready at all times.
