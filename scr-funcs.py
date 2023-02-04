from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_html(url):
    with sync_playwright() as pl:
        browser = pl.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("div#card_grid")
        return page.inner_html("div#card_grid")

def html_parser(html):
    list = []
    soup = bs(html, 'html.parser')
    items = soup.select("div.card-v2-wrapper")
    for i in items:
        heading2 = i.select_one("div.pad-hrz-xs h2.card-v2-title-wrapper a").text.strip()
        price = i.select_one("div.card-v2-content div.card-v2-pricing p.product-new-price").text.strip()
        href = i.select_one("div.card-v2-info a").attrs["href"]
        product = (heading2, price, href)
        list.append(product)
    return list
def main():
    gaming_url = "https://www.emag.bg/laptopi/filter/kapacitet-pamet-f7886,12-16-gb-v25916/kapacitet-pamet-f7886,nad-16-gb-v25917/tip-video-pamet-f7895,dopylnitelna-v-2754/tip-syhranenie-f7941,ssd-v-4670679/price,between-1000-and-3000/rating,star-4/c?ref=lst_leftbar_6420_4-5"
    gaming_html = get_html(gaming_url)
    gaming_list = html_parser(gaming_html)
    df = pd.DataFrame(gaming_list)
    print(df)

if __name__ == "__main__":
    main()