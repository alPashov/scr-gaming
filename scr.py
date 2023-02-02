from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs

url = 'https://www.emag.bg/laptopi/filter/kapacitet-pamet-f7886,12-16-gb-v25916/kapacitet-pamet-f7886,nad-16-gb-v25917/diagonal-displej-f7887,15-15-6-v25847/tip-video-pamet-f7895,dopylnitelna-v-2754/tip-syhranenie-f7941,ssd-v-4670679/video-chipset-f8356,nvidia-geforce-rtx-v-7220419/kapacitet-ssd-f9203,500-gb-v-4694038/kapacitet-ssd-f9203,1-tb-v-4690219/kapacitet-ssd-f9203,512-gb-v-4685751/price,between-1499-and-3000/c'

def get_html():
    with sync_playwright() as pl:
        browser = pl.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("div#card_grid")

        return page.inner_html("div#card_grid")