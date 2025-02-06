from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Kullanıcı adı ve şifre bilgilerinizi buraya girin
username = "ismail_ecrr"  # Instagram kullanıcı adınızı buraya girin
password = ".ismail.ecer.ismail"  # Şifrenizi buraya girin

# ChromeDriver yolunu belirtin
driver_path = r"C:\Driver\chromedriver.exe"

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Tarayıcıyı başlatma
        self.browser = webdriver.Chrome(driver_path)

    def sign_in(self):
        # Instagram giriş sayfasına git
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)  # Sayfanın yüklenmesini bekle

        # Kullanıcı adı ve şifre alanlarını bul
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        
        # Kullanıcı adını ve şifreyi yaz
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        # Şifre alanına Enter tuşuna basarak giriş yap
        password_input.send_keys(Keys.ENTER)

        # Giriş işleminin tamamlanmasını beklemek için biraz zaman tanı
        time.sleep(5)

        # Girişin başarılı olup olmadığını kontrol etmek için bir eleman kontrol edebilirsiniz
        try:
            self.browser.find_element(By.CLASS_NAME, "cmbtv")  # Varsayılan giriş sonrası pop-up
            print("Giriş başarılı!")
        except:
            print("Giriş yapılamadı.")

    def close_browser(self):
        self.browser.quit()

# Botu çalıştır
bot = InstagramBot(username, password)
bot.sign_in()
time.sleep(5)  # Biraz zaman tanıyın
bot.close_browser()
