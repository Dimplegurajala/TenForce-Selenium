
# TenForce QA Automation Project

This project automates a specific user journey on the TenForce Career page using **Python and Selenium**. [cite_start]It follows the **Page Object Model (POM)** to ensure the code is clean and easy to update[cite: 10].

##  How to Run the Test

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
Run the Test: Execute the following command to run the test and generate an HTML report:

Bash

pytest
The report will be saved in the reports/ folder.

🏗️ Architecture Explanation
I used the Page Object Model (POM) to separate the "What" (the test steps) from the "How" (the technical locators).


BasePage: Contains generic actions like clicking and scrolling.


CareerPage: Holds the specific XPaths and logic for TenForce.


This separation means if TenForce changes their website design, we only need to update one file (career_page.py) rather than fixing every single test.


## Engineering Decisions (Why I did what I did)
1. Solving the "Sticky Header" Problem
The TenForce website has a menu bar that stays at the top. Standard Selenium clicks often failed because the menu was "covering" the buttons. I solved this by creating a Scroll-to-Center function. This uses JavaScript to move the element to the middle of the screen before clicking, making sure the header never gets in the way.

2. Robust Locators (No Brittle XPaths)
Instead of using long, fragile XPaths like /div/div/h3, I used Text-Based Locators with normalize-space(). This makes the test "smart" enough to find the "Life of two interns" article even if the website developers change the layout slightly.

3. Meaningful Assertions
I didn't just check if the page loaded. The test specifically looks for the CV submission text ("Feel free to send your CV to") to confirm that the Job Openings section is fully functional.


4. Deterministic Navigation
Instead of relying on the browser's "Back" button (which can be unreliable), I used Direct URL Navigation to return to the career page. This ensures the test always starts the final assertion from a clean, known state.



---

### Final Push Instructions
1. Initialize your git repo: `git init`
2. Add your files: `git add .`
3. Commit: `git commit -m "Initial commit - TenForce Automation Suite"`
4. Push to your GitHub/GitLab link.