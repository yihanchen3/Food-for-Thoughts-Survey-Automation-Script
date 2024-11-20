# McDonald's Food for Thoughts Survey Automation Script

This Python script automates the completion of McDonald's Food for Thoughts surveys by selecting predefined options for each question and navigating through the survey pages. The script uses Selenium WebDriver to interact with the webpage.

## Features

- **Automated Selection**: Selects the second option for each question (e.g., "No" in Yes/No questions, "Satisfied" in Rating questions).
- **Dynamic Navigation**: Clicks the "Next" button to proceed through the survey.
- **Start Condition**: Begins automation upon detecting the question `"What was your visit type?"`.
- **End Condition**: Stops automation after detecting the question `"How would you like to receive your validation code to redeem your offer?"`.
- **Error Handling**: Handles common errors like unresponsive pages or missing elements.

## Prerequisites

1. Install Python 3.x.
2. Install Selenium:

   ```bash
   pip install selenium
   ```
3. Install a Google Chrome.

## Usage

1. **Set Up the Script** :

* Ensure the `chromedriver` executable is in your system's PATH or specify its location in the script.
* Modify the script to suit your preferences if needed (e.g., changing wait times or options).

2. **Run the Script** :

* Execute the script in your terminal or IDE:
  ```
  python mcd_survey_auto3.py
  ```
* The script will automatically open a Chrome and navigate to the *https://www.mcdfoodforthoughts.com/*.
* Press Continue and fill in the 12 digit code and amount of money on your receipt, then press Start to enter the survey.
* The script will start automation when detected the first question *'What was your visit type?'*, and end at the last question *'How would you like to receive your validation code to redeem your offer?'*.
* Select your way to receive the voucher, and the web will close itself when detected success message of "Thank you!"

3. **Manual Termination** :

* If you need to stop the script early, press `Ctrl+C` to terminate it gracefully in case of the Resource Leaks in WebDriver Sessions.

## Disclaimer

This script is intended for educational purposes only. Ensure compliance with McDonald's website terms of service when using automation tools.
