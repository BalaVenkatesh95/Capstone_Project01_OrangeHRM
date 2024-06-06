# tests/test_home_page.py
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.base_page import BasePage


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
file_path = "C:\\workspace\\orangeHR_TDD_POM\\resources\\login_details_positive.xlsx"
sheet_name = "login"

# Initialize HomePage object
base_page = BasePage(url)
login_page = LoginPage(base_page.driver)
home_page = HomePage(base_page.driver)

def test_TC03_PIM_create_employee():
    login_page.login_PIM(file_path, sheet_name)

    employee_data = {
        'first_name': 'John',
        'last_name': 'Doe'
    }
    home_page.create_employee(employee_data)

def test_TC_04_PIM_edit_employee():

    edit_data = {
        'otherid': 'PANID',
        'middlename': 'Dean'

    }
    home_page.edit_employee(edit_data)

def test_TC_05_PIM_delete_employee():
    home_page.delete_employee()

def test_shutdown():
    home_page.shutdown()
