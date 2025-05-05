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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wordpress-plugin-installation-test.git
