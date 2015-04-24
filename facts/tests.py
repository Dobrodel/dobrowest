# -*- coding: utf-8 -*-
import os

from django.core.urlresolvers import reverse
from django.test import Client
from django.test import LiveServerTestCase
from selenium.webdriver.safari.webdriver import WebDriver

# SELENIUM_SERVER_JAR = '/Users/dobrodel/Developer/envDjangoSite/lib/python2.7/site-packages/selenium/webdriver/safari/selenium-server-standalone-2.45.0.jar'
#import os

#os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = '127.0.0.1:8000'

class AuthorsTest(LiveServerTestCase):
	@classmethod
	def setUpClass( cls ):
		cls.selenium = WebDriver()
		super(AuthorsTest, cls).setUpClass()

	@classmethod
	def tearDownClass( cls ):
		cls.selenium.quit()
		super(AuthorsTest, cls).tearDownClass()

	def test_login( self ):
		drv = self.selenium
		user = Client()
		try
			login_url = reverse('account_login', args = [])
		user.post(login_url, { 'login': 'adam', 'password': '12345' })
		#self.selenium.get(os.path.join(self.live_server_url, reverse('facts:detail', args = [3])))
		drv.get(os.path.join(self.live_server_url, reverse('facts:detail', args = [1])))
		drv.find_element_by_name('foto')

	#sel.set_script_timeout(10)
	#sel.find_element_by_name('login').send_keys('adam')
	##sel.find_element_by_name('password').send_keys('12345')
	#sel.find_element_by_name('remember').click()
	#sel.find_element_by_class_name('primaryAction').submit()


'''
<form class="login" method="POST" action="/accounts/login/">
    <input type='hidden' name='csrfmiddlewaretoken' value='8sRkyZtTrX2jthPxCsVzXUDvTonFsPHA' />
    <p><label for="id_login">Имя пользователя:</label>
        <input autofocus="autofocus" id="id_login" maxlength="30" name="login" placeholder="Имя пользователя" type="text" /></p>
	<p><label for="id_password">Пароль:</label>
		<input id="id_password" name="password" placeholder="Пароль" type="password" /></p>

	<p><label for="id_remember">Запомнить меня:</label>
		<input id="id_remember" name="remember" type="checkbox" /></p>

    <a class="button secondaryAction" href="/accounts/password/reset/">
        Забыли пароль?
    </a>
    <button class="primaryAction" type="submit">
        Войти
    </button>
</form>

        self.selenium.get(os.path.join(self.live_server_url, reverse('facts:detail', args = [3])))
		self.selenium.find_element_by_link_text('add contact').click()

		self.selenium.find_element_by_id('id_first_name').send_keys('test')
		self.selenium.find_element_by_id('id_last_name').send_keys('contact')
		self.selenium.find_element_by_id('id_email').send_keys('test@example.com')

		self.selenium.find_element_by_id('save_contact').click()
		self.assertEqual(
			self.selenium.find_elements_by_css_selector('.contact')[-1].text,
			'test contact'
		)
 '''
# Create your tests here.
