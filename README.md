# TenForce QA Automation Project - Selenium & Performance Suite

This repository contains a professional-grade automation ecosystem for the TenForce Career page user journey. It is designed to be resilient, environment-agnostic, and scalable by incorporating a Service Layer for hermetic testing and a Reliability Layer for performance benchmarking.

## How to Run the Suite
### 1. Install Dependencies
Bash

pip install -r requirements.txt
### 2. Run Functional UI Tests (Selenium)
This command runs the Selenium suite headlessly and generates a self-contained HTML report in the reports/ folder.

Bash

pytest --html=reports/selenium_report.html --self-contained-html

### 3. Run Performance Tests (Locust)
First, start the mock service layer:

Bash

python mocks/mock_server.py

In a second terminal, execute the load test (configured for 10 concurrent users):

Bash

locust -f performance/locustfile.py --headless -u 10 -r 2 -t 30s --html reports/performance_report.html

## Architecture & Engineering Decisions
I implemented a Three-Tier Testing Architecture to ensure the suite provides maximum value across the software development life cycle (SDLC).

### 1. Functional Layer (Page Object Model)
I utilized a strict POM to separate test logic from locators, ensuring high maintainability.

BasePage Engine: Contains resilient interaction logic, such as a JavaScript-based Scroll-to-Center function to bypass the Sticky Header that often intercepts standard Selenium clicks.

Robust Locators: Utilized text-based locators with normalize-space() to ensure tests remain stable even if the underlying HTML structure changes.

### 2. Service Layer (Hermetic Mocks)
To ensure the CI/CD pipeline is not dependent on the external uptime of tenforce.com, I developed a Flask Mock Server.

This facilitates Shift-Left testing, allowing for API validation before the UI is even deployed.

It ensures a deterministic environment where test failures are caused by code issues, not environment instability.

### 3. Reliability Layer (Locust Performance)
Performance is treated as a core feature. I integrated Locust to benchmark backend stability.

Baseline Validation: Successfully achieved 6.2 Requests Per Second with 0% failures.

Latency Monitoring: Maintained a stable p99 response time of 130ms, validating that the system handles concurrent traffic without degradation.

## CI/CD Pipeline (GitHub Actions)
The project is fully integrated with GitHub Actions. Every push triggers a headless Linux runner that:

- **Spins up the Service Layer (Mock Server).**

- **Executes the Functional Suite (Selenium).**

- **Runs the Reliability Benchmark (Locust).**

- **Artifact Management**: All results are archived in a dedicated reports/ directory with a 15-day retention policy, keeping the main repository 100% Python code.