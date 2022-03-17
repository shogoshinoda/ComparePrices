from django.shortcuts import render
from django.views.generic.base import TemplateView
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from .forms import CompareForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_keyword(self):
        keyword = self.request.GET.get('keyword')
        return keyword

    @property
    def amazon_scraping(self):
        options = Options()
        options.add_argument('--headless')
        keyword = self.get_keyword()
        browser = webdriver.Chrome(options=options, executable_path='/Users/shinodashogo/Documents/Python'
                                                                    '/chromedriver/chromedriver')
        amazon_url = 'https://www.amazon.co.jp/'
        browser.get(amazon_url)
        sleep(1)
        elem_search = browser.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
        elem_search.send_keys(keyword)
        elem_click = browser.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
        elem_click.click()
        sleep(1)
        amazon_products = [[], [], []]
        elems_product_name = browser.find_elements_by_class_name('a-size-base-plus.a-color-base.a-text-normal')
        elems_product_price = browser.find_elements_by_class_name('a-price-whole')
        elems_product_url = browser.find_elements_by_class_name('a-link-normal.s-underline-text.s-underline-link'
                                                                '-text.s-link-style.a-text-normal')
        len_elem = len(elems_product_name)
        if len_elem >= 10:
            loop_num = 10
        else:
            loop_num = len_elem
        for i in range(loop_num):
            amazon_products[0].append(elems_product_name[i].text)
            amazon_products[1].append(elems_product_price[i].text)
            amazon_products[2].append(elems_product_url[i].get_attribute('href'))
        browser.quit()
        return amazon_products

    def rakuten_scraping(self):
        options = Options()
        options.add_argument('--headless')
        keyword = self.get_keyword()
        browser = webdriver.Chrome(options=options, executable_path='/Users/shinodashogo/Documents/Python'
                                                                    '/chromedriver/chromedriver')
        rakuten_url = 'https://www.rakuten.co.jp/'
        browser.get(rakuten_url)
        sleep(1)
        elem_search = browser.find_element_by_xpath('//*[@id="common-header-search-input"]')
        elem_search.send_keys(keyword)
        elem_click = browser.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div/div/div['
                                                   '1]/div/div/div/a/div/div/div')
        elem_click.click()
        sleep(1)
        rakuten_products = [[], [], []]
        elems_product_price = browser.find_elements_by_class_name('important')
        elems_product_name = browser.find_elements_by_css_selector('div.content div.title h2')
        elems_product_url = browser.find_elements_by_css_selector('div.content div.title a')
        len_elem = len(elems_product_name)
        if len_elem >= 10:
            loop_num = 10
        else:
            loop_num = len_elem
        for i in range(loop_num):
            rakuten_products[0].append(elems_product_name[i].text)
            rakuten_products[1].append(elems_product_price[i].text)
            rakuten_products[2].append(elems_product_url[i].get_attribute('href'))
        browser.quit()
        return rakuten_products

    def yahoo_scraping(self):
        options = Options()
        options.add_argument('--headless')
        keyword = self.get_keyword()
        browser = webdriver.Chrome(options=options, executable_path='/Users/shinodashogo/Documents/Python'
                                                                    '/chromedriver/chromedriver')
        yahoo_url = 'https://shopping.yahoo.co.jp/'
        browser.get(yahoo_url)
        sleep(1)
        elem_search = browser.find_element_by_xpath('//*[@id="ss_yschsp"]')
        elem_search.send_keys(keyword)
        elem_click = browser.find_element_by_xpath('//*[@id="ss_srch_btn"]')
        elem_click.click()
        sleep(1)
        yahoo_products = [[], [], []]
        elems_product_price = browser.find_elements_by_class_name('_3-CgJZLU91dR')
        elems_product_name = browser.find_elements_by_class_name('_2EW-04-9Eayr')
        elems_product_url = browser.find_elements_by_css_selector('a._2EW-04-9Eayr')
        len_elem = len(elems_product_name)
        if len_elem >= 10:
            loop_num = 10
        else:
            loop_num = len_elem
        for i in range(loop_num):
            yahoo_products[0].append(elems_product_name[i].text)
            yahoo_products[1].append(elems_product_price[i].text)
            yahoo_products[2].append(elems_product_url[i].get_attribute('href'))
        browser.quit()
        return yahoo_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        keyword = self.get_keyword()
        if keyword:
            amazon_products = self.amazon_scraping
            rakuten_products = self.rakuten_scraping()
            yahoo_products = self.yahoo_scraping()
            context['amazon_products'] = amazon_products
            context['rakuten_products'] = rakuten_products
            context['yahoo_products'] = yahoo_products
        context['keyword'] = keyword
        return context
