from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()
actions = ActionChains(driver)

def select_second_option_and_next():
    try:
        # Find all radio buttons on the page
        radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
        
        # Track the questions we have already processed
        processed_questions = set()
        
        # Dictionary to store the radio buttons by question name
        question_options = {}
        
        for radio_button in radio_buttons:
            question_name = radio_button.get_attribute("name")
            if question_name not in question_options:
                question_options[question_name] = []
            question_options[question_name].append(radio_button)
        
        for question_name, options in question_options.items():
            if len(options) >= 2:
                # Select the second option for the question
                driver.execute_script("arguments[0].click();", options[1])
                processed_questions.add(question_name)
            else:
                logging.warning(f"Not enough options for question {question_name}")
        
        # Find the "Next" button and click it using JavaScript
        # Wait for the "Next" button to be clickable
        next_button = driver.find_element(By.ID, 'NextButton')
        actions.move_to_element(next_button).click().perform()

    except Exception as e:
        logging.error(f"Error selecting option: {e}")

def check_page_status():
    try:
        # Check for common indicators of a failed page load
        if "This page isn't working" in driver.title or "HTTP ERROR 504" in driver.page_source:
            logging.error("Webpage is unresponsive. HTTP ERROR 504.")
            return False
    except Exception as e:
        logging.error(f"Error checking page status: {e}")
        return False
    return True

if __name__ == "__main__":
    try:
        # Open the survey page
        driver.get('https://www.mcdfoodforthoughts.com/')
        logging.info("Opened survey page.")
        print("Notice: Please fill in the 12 digit code and click 'Next' to start the survey.")

        # Wait for the first question of survey to start automation
        start_question = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//legend[text()='What was your visit type?']"))
        )
        
        if start_question:
            logging.info("Survey Question detected. Starting automation...")
            
            while True:
                end_question = driver.find_elements(By.XPATH, "//legend[contains(text(), 'How would you like to receive your validation code to redeem your offer?')]")
                # if the last question is detected, break the loop, and wait 
                if end_question:
                    logging.info("Survey Completed. Stopping automation.")
                    print('Notice: Please choose the option to receive the validation code and click "Next" to complete the survey.')
                    break

                elif not check_page_status():
                    logging.error("Page unresponsive. Refreshing...")
                    # driver.refresh()
                    current_url = driver.current_url
                    driver.get(current_url)
                    time.sleep(4)
                    continue

                select_second_option_and_next()
                time.sleep(2)
            
            # Wait for the final page including "thank you" as a sign of completion
            success_flag = WebDriverWait(driver, 200).until(
            EC.presence_of_element_located((By.XPATH,  "//h2[contains(text(), 'Thank You!')]"))
            )
            if success_flag:
                logging.info("Voucher acquired successfully.")
                print("Notice: WebDriver closed in 10 seconds.")
                time.sleep(10)
            else:
                logging.error("Voucher not acquired. Try again.")

        else:
            logging.error("Survey page not detected. Exiting script.")

    except KeyboardInterrupt:
        # remember to end the script early with Ctrl+C if needed, to clean up the WebDriver
        print("Script terminated by user (Ctrl+C). Cleaning up...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

    finally:
        # Ensure the driver is closed, even if an error occurs, in case of Resource Leaks in WebDriver Sessions that can cause the browser to timeout 504
        driver.quit()
        logging.info("WebDriver closed.")
