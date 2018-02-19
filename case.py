# -*- coding: utf-8 -*-

from module import *

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.n11.com/")
        self.driver.maximize_window()
        return self.driver

    def test_search(self):
        pagetitle = self.driver.title
        assert "n11.com" in pagetitle
        self.driver.find_element_by_class_name("btnSignIn").click()
        self.driver.find_element_by_id("email").send_keys("yalcinkaya93@gmail.com")
        self.driver.find_element_by_id("password").send_keys("123456a")
        self.driver.find_element_by_id("loginButton").click()
        self.driver.find_element_by_id("searchData").send_keys("samsung")
        self.driver.find_element_by_class_name("searchBtn").click()
        pagecode = self.driver.page_source
        self.assertNotEquals(pagecode, "notFoundContainer", "")
        self.driver.find_element_by_link_text("2").click()
        pageurl = self.driver.current_url
        assert "pg=2" in pageurl
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@data-position='31']/div[@class='pro']/a").click()
        thirdurl = self.driver.current_url
        time.sleep(1)
        self.driver.find_element_by_id("getWishList").click()
        time.sleep(1)
        self.driver.find_element_by_id("addToFavouriteWishListBtn").click()
        self.driver.get("https://www.n11.com/hesabim/favorilerim")
        assert "samsung-note3-n9000-orginal-batarya-note-3-n9000q" in thirdurl
        self.driver.find_element_by_xpath("//div[@class='wishProBtns']/span[@class='deleteProFromFavorites']").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("//div[@class='btnHolder']/span[@class='btn btnBlack confirm']").click()
        print("test ok")

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()


