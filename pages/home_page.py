# pages/home_page.py
import time
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.helpers import wait_for_element, element_clickable, wait_for_element_presence
from utils.screenshot import take_screenshot

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def create_employee(self, employee_data):
        self.pim_button = "//span[text()='PIM']"
        self.add_button = "//button[@type='button' and .//i[@class='oxd-icon bi-plus oxd-button-icon'] and contains(., 'Add')]"
        self.first_name_field = "//input[@name='firstName' and @placeholder='First Name']"
        self.middle_name_field = "//input[@name='middleName' and @placeholder='Middle Name']"
        self.last_name_field = "//input[@name='lastName' and @placeholder='Last Name']"
        self.save_button = "//button[@type='submit' and normalize-space()='Save']"



        element_clickable(self.driver, self.pim_button)
        self.click_element(self.pim_button)

        element_clickable(self.driver, self.add_button)
        self.click_element(self.add_button)

        wait_for_element(self.driver, self.first_name_field)
        self.enter_text(self.first_name_field, employee_data['first_name'])

        wait_for_element(self.driver, self.last_name_field)
        self.enter_text(self.last_name_field, employee_data['last_name'])
        time.sleep(10)
        wait_for_element_presence(self.driver, self.save_button)
        element_clickable(self.driver, self.save_button)
        self.click_element(self.save_button)
        take_screenshot(self.driver)



    def edit_employee(self, edit_data):
        self.search_employee_id_field = "//label[@class='oxd-label' and text()='Employee Id']/following::input[@class='oxd-input oxd-input--active'][1]"
        self.search_button = "//button[@type='submit' and normalize-space()='Search']"
        self.result_found = "//span[text()='(1) Record Found']"
        self.edit_button = "//i[@class='oxd-icon bi-pencil-fill']"
        self.otherid_field = "//label[@class='oxd-label' and text()='Other Id']/following::input[@class='oxd-input oxd-input--active'][1]"
        self.middle_name_field = "//input[@name='middleName' and @placeholder='Middle Name']"
        self.gender_male_button = "//input[@type='radio' and @value='1']"
        self.save_button_edit_page = "(//button[@type='submit' and normalize-space()='Save'])[1]"

        self.employee_id_field = "(//div[@data-v-957b4417]/input[@class='oxd-input oxd-input--active'])[1]"


        wait_for_element_presence(self.driver, self.employee_id_field)
        employee_id = self.extract_employee_id(self.employee_id_field)
        print(employee_id)

        element_clickable(self.driver, self.pim_button)
        self.click_element(self.pim_button)

        wait_for_element(self.driver, self.search_employee_id_field)
        self.enter_text(self.search_employee_id_field, employee_id)

        element_clickable(self.driver, self.search_button)
        self.click_element(self.search_button)

        wait_for_element_presence(self.driver, self.result_found)
        self.scroll_down()

        wait_for_element(self.driver, self.edit_button)
        self.click_element(self.edit_button)

        wait_for_element_presence(self.driver, self.otherid_field)
        self.enter_text(self.otherid_field, edit_data['otherid'])
        wait_for_element_presence(self.driver, self.middle_name_field)
        self.enter_text(self.middle_name_field, edit_data['middlename'])


        self.scroll_down()
        time.sleep(10)
        wait_for_element_presence(self.driver, self.save_button_edit_page)
        self.click_element(self.save_button_edit_page)
        take_screenshot(self.driver)



    def delete_employee(self):

        self.delete_button = "//i[@class='oxd-icon bi-trash']"
        self.no_results_found = "//span[text()='No Records Found']"
        self.result_found = "//span[text()='(1) Record Found']"
        self.yes_delete_button = "//button[@type='button' and contains(@class, 'oxd-button--label-danger') and contains(., 'Yes, Delete')]"

        wait_for_element_presence(self.driver, self.employee_id_field)
        employee_id = self.extract_employee_id(self.employee_id_field)

        wait_for_element_presence(self.driver, self.pim_button)
        element_clickable(self.driver, self.pim_button)
        self.click_element(self.pim_button)

        wait_for_element(self.driver, self.search_employee_id_field)
        self.enter_text(self.search_employee_id_field, employee_id)

        element_clickable(self.driver, self.search_button)
        self.click_element(self.search_button)


        wait_for_element_presence(self.driver, self.result_found)
        self.scroll_down()

        wait_for_element(self.driver, self.delete_button)
        self.click_element(self.delete_button)


        wait_for_element_presence(self.driver, self.yes_delete_button)
        self.handle_popup(self.yes_delete_button)
        take_screenshot(self.driver)

