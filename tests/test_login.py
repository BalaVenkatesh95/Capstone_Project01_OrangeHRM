from pages.login_page import LoginPage
from pages.base_page import BasePage

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


file_path_positive = "C:\\workspace\\orangeHR_TDD_POM\\resources\\login_details_positive.xlsx"
file_path_negative = "C:\\workspace\\orangeHR_TDD_POM\\resources\\login_details_negative.xlsx"
sheet_name = "login"


base_page = BasePage(url)
login_page = LoginPage(base_page.driver)

def test_TC01_login():
    login_page.login_user(file_path_positive, sheet_name)

def test_TC02_negativelogin():
    login_page.login_user(file_path_negative, sheet_name)

def test_shutdown():
    login_page.shutdown()
