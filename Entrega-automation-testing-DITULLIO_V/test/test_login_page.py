import pytest
from page.login_page import LoginPage
from data.data_login import PRUEBAS_LOGUIN


@pytest.mark.parametrize("username,password,login_bool",PRUEBAS_LOGUIN)
def test_loguin (driver, username,password,login_bool):
    loginPage = LoginPage (driver)
    loginPage.open ()
    loginPage.login(username , password)

