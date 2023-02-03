from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
import time

url = "https://www.emag.bg/laptopi/filter/kapacitet-pamet-f7886,12-16-gb-v25916/kapacitet-pamet-f7886,nad-16-gb-v25917/diagonal-displej-f7887,15-15-6-v25847/tip-video-pamet-f7895,dopylnitelna-v-2754/tip-syhranenie-f7941,ssd-v-4670679/video-chipset-f8356,nvidia-geforce-rtx-v-7220419/kapacitet-ssd-f9203,500-gb-v-4694038/kapacitet-ssd-f9203,1-tb-v-4690219/kapacitet-ssd-f9203,512-gb-v-4685751/price,between-1499-and-3000/c"

def get_html():
    with sync_playwright() as pl:
        browser = pl.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("div#card_grid")

        return page.inner_html("div#card_grid")
    

def html_parser(html):

    soup = bs(html, 'html.parser')

    items = soup.select("div.pad-hrz-xs")

    links = []
    for i in items:
        href = i.select_one("h2.card-v2-title-wrapper a").attrs["href"]
        links.append(href)
    return links

def csv_export(links):
    with open("links.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Link"])
        for href in links:
            writer.writerow([href])

def pd_csv():
    pandas_csv = pd.read_csv("links.csv")
    print(pandas_csv)


def debugPrinting(links):
    print("Pandas printing from links.csv :")
    pd_csv()
    print("links list output:")
    print(links)



def main():
    html = get_html()
    links = html_parser(html)
    csv_export(links)
    debugPrinting(links)

def autoRun():
    while True:
        html = get_html()
        links = html_parser(html)
        csv_export(links)
        debugPrinting(links)
        
        time.sleep(3600)

if __name__ == "__main__":
    main()