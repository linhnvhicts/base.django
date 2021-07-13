from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from backend.models import User


class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        user = User.objects.create(
            username="admin", email="admin@mpt.vn", is_staff=True, is_superuser=True)
        user.set_password('123456')
        user.save()

        super().setUpClass()
        try:
            WebDriver().implicitly_wait(10)
        except Exception as e:
            print(e)

    @classmethod
    def tearDownClass(cls):
        WebDriver().quit()
        super().tearDownClass()

    def test_login(self):
        WebDriver().get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = WebDriver().find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = WebDriver().find_element_by_name("password")
        password_input.send_keys('123456')
        WebDriver().find_element_by_xpath('//input[@value="Log in"]').click()
