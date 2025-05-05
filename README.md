# WordPress Plugin Automation Testing: Everest Forms

This repository contains end-to-end tests for automating the installation, activation, and verification of the **Everest Forms** plugin on a local WordPress setup using **Selenium** and **Pytest**.

## Task Description
The tests automate the following steps:
1. Navigate to the WordPress login page and input the required credentials.
2. Go to the "Plugins" section.
3. Proceed to the "Add New" plugin page.
4. Search for the "Everest Forms" plugin.
5. Install the "Everest Forms" plugin.
6. Activate the plugin.
7. Verify the presence of the "Welcome to Everest Forms" message.

## Prerequisites
- **WordPress** installed and running locally (e.g., via XAMPP).
- **Python 3.x** installed.
- **Selenium** WebDriver and the **Chrome WebDriver** configured.
- **pytest** and **pytest-selenium** installed.
- **Chrome** (or other browsers) installed for the tests.

## Report Generation
The test results are stored in a report.html file. You can open this file in any browser to view the test results and logs in an easy-to-read format. The report includes:

- A summary of passed/failed tests.

- Detailed information for each test step.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wordpress-plugin-installation-test.git


2. Setting Up Environment Variables

To securely store sensitive information, such as the WordPress login credentials, I have created a `.env` file in the root of the project with the following content:

```ini
WP_USERNAME=your-username-here
WP_PASSWORD=your-password-here


