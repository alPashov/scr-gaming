from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd

urls = [
    #Gaming Links 
    "https://www.emag.bg/laptopi/filter/kapacitet-pamet-f7886,12-16-gb-v25916/kapacitet-pamet-f7886,nad-16-gb-v25917/tip-video-pamet-f7895,dopylnitelna-v-2754/tip-syhranenie-f7941,ssd-v-4670679/price,between-1000-and-3000/rating,star-4/c?ref=lst_leftbar_6420_4-5",
    #Everyday/Home
    "https://www.emag.bg/laptopi/filter/kapacitet-pamet-f7886,6-8-gb-v25915/tip-video-pamet-f7895,vgradena-v-2755/price,between-500-and-1000/rating,star-4/c?ref=lst_leftbar_6420_4-5",
    #Office
    "https://www.emag.bg/laptopi/filter/kapacitet-pamet-f7886,12-16-gb-v25916/tip-video-pamet-f7895,vgradena-v-2755/avtonomija-baterija-f7901,nad-6-h-v25862/tip-syhranenie-f7941,ssd-v-4670679/kapacitet-ssd-f9203,500-gb-v-4694038/kapacitet-ssd-f9203,1-tb-v-4690219/kapacitet-ssd-f9203,512-gb-v-4685751/price,between-979-and-5732/rating,star-4/c"

]

def get_html():
    htmls = []
    with sync_playwright() as pl:
        browser = pl.firefox.launch(headless=False)
        page = browser.new_page()
        for u in urls:
            page.goto(u)
            page.wait_for_selector("div#card_grid")
            htmls.append(page.inner_html("div#card_grid"))
    return htmls

def html_parsers(htmls):
    links = []
    for h in htmls:
        soups = bs(h, "html.parser")
        items = soups.select("div.pad-hrz-xs")

        for i in items:
            href = i.select_one("h2.card-v2-title-wrapper a").attrs["href"]
            links.append(href)
    
        # links.append(href)
    return links

def csv_export(links):
    with open("links_all.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Link"])
        for href in links:
            writer.writerow([href])


def main():
    htmls = get_html()
    links = html_parsers(htmls)
    csv_export(links)

if __name__ == "__main__":
    main()