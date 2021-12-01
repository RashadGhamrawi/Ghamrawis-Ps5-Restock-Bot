from selenium import webdriver
from selenium.webdriver.common.by import *
import smtplib
from info import *

my_email = my_email
password = password
receiver = receiver

chrome_driver_path = "/Users/rashad/Development/chromedriver"  # Your Chrome Path
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')


class Ps5:
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_driver_path, options=options)
        self.browser.set_page_load_timeout(60)
        self.is_available = ""
        self.is_available_2 = ""
        self.is_available_3 = ""
        self.is_available_4 = ""
        self.is_available_5 = ""
        self.is_available_6 = ""
        self.is_available_7 = ""
        self.is_available_8 = ""
        self.is_available_9 = ""
        self.is_available_10 = ""
        self.is_available_11 = ""
        self.is_available_12 = ""

        def ps5_a(name):
            self.browser.get('https://books.rakuten.co.jp/rb/16462859/?bkts=1')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "ご注文できない商品*" in all_span:
                print(f"{name}　NOT in stock")
                self.is_available = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!PS5 Disc Edition in stock!!!!!!!!!\n\nBuy it from "
                                            "here https://books.rakuten.co.jp/rb/16462859/?bkts=1")
                self.is_available = True

        def ps5_b(name):
            self.browser.get('https://books.rakuten.co.jp/rb/16462860/?bkts=1')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "ご注文できない商品*" in all_span:
                print(f"{name}　NOT in stock")
                self.is_available_2 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Digital Edition in stock!!!!!!!!!!\n\nBuy it "
                                            "from here https://books.rakuten.co.jp/rb/16462860/?bkts=1")
                self.is_available_2 = True

        def ps5_c(name):
            self.browser.get('https://www.amazon.co.jp/PlayStation-CFI-1000A01-%E3%83%91%E3%83%A9%E3%83%AC%E3%83%AB%E3%'
                             '83%BB%E3%83%88%E3%83%A9%E3%83%96%E3%83%AB-ECJS-00008-%E3%82%BB%E3%83%83%E3%83%88%E3%80%'
                             '90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB%'
                             'E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%82%A8%E3%82%B3%E3%83%90%E3%83%83%E3%82%B0/dp/B09'
                             '5HKG74J/ref=lp_8019285051_1_6?language=en_US')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock Amazon")
                self.is_available_3 = False
            else:
                print(f"{name}　is in stock Amazon!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!PS5 Disc Edition ratchet and clank in "
                                            "stock!!!!!!!!!\n\nBuy it from here https://www.amazon.co.jp/PlayStation"
                                            "-CFI-1000A01-%E3%83%91%E3%83%A9%E3%83%AC%E3%83%AB%E3%83%BB%E3%83%88%E3%8"
                                            "3%A9%E3%83%96%E3%83%AB-ECJS-00008-%E3%82%BB%E3%83%83%E3%83%88%E3%80%90"
                                            "Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91%E3%82%AA%E3%83%AA%E3%82%B8%E3%8"
                                            "3%8A%E3%83%AB%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%82%A8%E3%82%B3%E3%83"
                                            "%90%E3%83%83%E3%82%B0/dp/B095HKG74J/ref=lp_8019285051_1_6?language=en_US")

                self.is_available_3 = True

        def ps5_d(name):
            self.browser.get('https://www.amazon.co.jp/PlayStation-Tales-ARISE-ELJS-20006-%E3%82%BB%E3%83%83%E3%83%88'
                             '%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91%E3%82%A2%E3%82%BF%E3%83%83%E3%83%81%E3'
                             '%83%A1%E3%83%B3%E3%83%88%E3%80%8C%E8%96%94%E8%96%87%E3%81%AE%E3%83%95%E3%83%AB%E3%83%AB'
                             '%E4%BA%BA%E5%BD%A2%E3%80%8D%E3%81%8C%E5%85%A5%E6%89%8B%E3%81%A7%E3%81%8D%E3%82%8B%E3%83'
                             '%97%E3%83%AD%E3%83%80%E3%82%AF%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89/dp/B09CTLPY23/ref=lp_'
                             '8019285051_1_5')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock Amazon")

                self.is_available_4 = False
            else:
                print(f"{name}　is in stock Amazon !!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Disc Edition Tales of ARISE in stock!!!!!!!!!!\n\n"
                                            "Buy it from here https://www.amazon.co.jp/PlayStation-Tales-ARISE-ELJS-20"
                                            "006-%E3%82%BB%E3%83%83%E3%83%88%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3"
                                            "%80%91%E3%82%A2%E3%82%BF%E3%83%83%E3%83%81%E3%83%A1%E3%83%B3%E3%83%88%E3%"
                                            "80%8C%E8%96%94%E8%96%87%E3%81%AE%E3%83%95%E3%83%AB%E3%83%AB%E4%BA%BA%E5%BD"
                                            "%A2%E3%80%8D%E3%81%8C%E5%85%A5%E6%89%8B%E3%81%A7%E3%81%8D%E3%82%8B%E3%83%9"
                                            "7%E3%83%AD%E3%83%80%E3%82%AF%E3%83%88%E3%82%B3%E3%83%BC%E3%83%89/dp/B09CTL"
                                            "PY23/ref=lp_8019285051_1_5")
                self.is_available_4 = True

        def ps5_e(name):
            self.browser.get('https://www.amazon.co.jp/PlayStation-CFI-1000A01-Marvels-Spider-Man-%E3%82%BB%E3%83%83%'
                             'E3%83%88%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91%E3%82%AA%E3%83%AA%E3%82%B8%E3%8'
                             '3%8A%E3%83%ABPC%E5%A3%81%E7%B4%99/dp/B091D2HGKP/ref=lp_8019285051_1_9')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock")
                self.is_available_5 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Disc Spider man Edition in stock!!!!!!!!!!\n\nBuy "
                                            "it from here https://www.amazon.co.jp/PlayStation-CFI-1000A01-Marvels-Sp"
                                            "ider-Man-%E3%82%BB%E3%83%83%E3%83%88%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%"
                                            "9A%E3%80%91%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%ABPC%E5%A3%81%E7%B4%"
                                            "99/dp/B091D2HGKP/ref=lp_8019285051_1_9")

                self.is_available_5 = True

        def ps5_f(name):
            self.browser.get('https://www.amazon.co.jp/-/en/dp/B091D2959B/ref=sr_1_13?qid=1637147973&s=videogames&'
                             'sr=1-13')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock")
                self.is_available_6 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Disc Demon souls Edition in stock!!!!!!!!!!\n\nBuy "
                                            "it from here https://www.amazon.co.jp/-/en/dp/B091D2959B/ref=sr_1_13?qid"
                                            "=1637147973&s=videogames&sr=1-13")

                self.is_available_6 = True

        def ps5_g(name):
            self.browser.get(
                'https://www.amazon.co.jp/-/en/CFI-1000A01/dp/B08GGGCH3Y/ref=sr_1_12?qid=1637147973&s=videogames&sr'
                '=1-12')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock")
                self.is_available_7 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Disc Original Edition in stock!!!!!!!!!!\n\nBuy it"
                                            " from here https://www.amazon.co.jp/-/en/CFI-1000A01/dp/B08GGGCH3Y/ref=s"
                                            "r_1_12?qid=1637147973&s=videogames&sr=1-12")

                self.is_available_7 = True

        def ps5_h(name):
            self.browser.get(
                'https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E'
                '3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3'
                '%83%B3%E3%83%88-PlayStation-5-CFI-1000A01/dp/B08GGGBKRQ/ref=lp_8019285051_1_8')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock")
                self.is_available_8 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Disc Original 2 Edition in stock!!!!!!!!!!\n\nBuy it"
                                            " from here https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%"
                                            "E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E"
                                            "3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3"
                                            "%83%88-PlayStation-5-CFI-1000A01/dp/B08GGGBKRQ/ref=lp_8019285051_1_8")

                self.is_available_8 = True

        def ps5_i(name):
            self.browser.get('https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%B'
                             'F%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%8'
                             '2%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3%83%88-PlayStation-5-CFI-1100A01/dp/B09CTQPQNV/ref=lp'
                             '_8019285051_1_3')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock")

                self.is_available_9 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Disc Original 3 Edition in stock!!!!!!!!!!\n\nBuy it"
                                            " from here https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%"
                                            "E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E"
                                            "3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3"
                                            "%83%88-PlayStation-5-CFI-1100A01/dp/B09CTQPQNV/ref=lp_8019285051_1_3")
                self.is_available_9 = True

        def ps5_j(name):
            self.browser.get('https://www.amazon.co.jp/-/en/dp/B09CTP3M5D/ref=sr_1_7?qid=1637147973&s=videogames&sr='
                             '1-7')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "Currently unavailable." in all_span:
                print(f"{name}　NOT in stock")

                self.is_available_10 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!!!PS5 Disc ratchet and clank bag Edition in stock!!!!!!"
                                            "!!!!\n\nBuy it from here https://www.amazon.co.jp/-/en/dp/B09CTP3M5D/re"
                                            "f=sr_1_7?qid=1637147973&s=videogames&sr=1-7")
                self.is_available_10 = True

        def ps5_k(name):
            self.browser.get('https://books.rakuten.co.jp/rb/16842146/?bkts=1')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "ご注文できない商品*" in all_span:
                print(f"{name}　NOT in stock")
                self.is_available_11 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!PS5 Disc Edition in stock!!!!!!!!!\n\nBuy it from here"
                                            " https://books.rakuten.co.jp/rb/16462859/?bkts=1")
                self.is_available_11 = True

        def ps5_l(name):
            self.browser.get('https://books.rakuten.co.jp/rb/16815674/?bkts=1')

            all_span = self.browser.find_elements(By.CSS_SELECTOR, "span")
            all_span = [i.text for i in all_span]

            if "ご注文できない商品*" in all_span:
                print(f"{name}　NOT in stock")
                self.is_available_12 = False
            else:
                print(f"{name}　is in stock!!!!!!!!!!!!!")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=receiver,
                                        msg="Subject:!!!!!!!PS5 Digital Edition in stock!!!!!!!!!\n\nBuy it from here"
                                            " https://books.rakuten.co.jp/rb/16462859/?bkts=1")
                self.is_available_12 = True

        ps5_a("PS5通常版 Rakuten")
        ps5_b("PS5デジタル版 Rakuten")
        ps5_c("PS5通常版 ratchet and clank Amazon")
        ps5_d("PS5通常版 Tales-ARISE Amazon")
        ps5_e("PS5通常版 Spider-Man Amazon")
        ps5_f("PS5通常版 Demon-Souls Amazon")
        ps5_g("PS5通常版 Original Amazon")
        ps5_h("PS5通常版 Original 2 Amazon")
        ps5_i("PS5通常版 Original 3 Amazon")
        ps5_j("PS5通常版 ratchet and clank bag Amazon")
        ps5_k("New PS5通常版 Rakuten")
        ps5_l("New PS5デジタル版 Rakuten")

        self.browser.close()
