import asyncio
import json
from xml.dom import minidom

import aiohttp
from bs4 import BeautifulSoup

main_page_url = "https://markets.businessinsider.com/index/components/s&p_500?p="


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def parsing():
    stocks = []
    loop = asyncio.get_event_loop()
    u = loop.run_until_complete(get("http://www.cbr.ru/scripts/XML_daily.asp"))
    dom = minidom.parseString(u)
    dom.normalize()
    usd = float(dom.getElementsByTagName("Value")[10].firstChild.data.replace(",", "."))

    for i in range(1, 11):
        main_page = loop.run_until_complete(get(main_page_url + str(i)))
        soup = BeautifulSoup(main_page, "html.parser")

        for j, stock in enumerate(soup.find(class_="table table-small").find_all("a")):
            stock_page = loop.run_until_complete(
                get("https://markets.businessinsider.com" + stock["href"])
            )
            sp = BeautifulSoup(stock_page, "html.parser")
            company_code = (
                sp.find(class_="price-section__category").span.get_text().strip(", ")
            )
            try:
                p_e = float(
                    sp.find("div", string="P/E Ratio")
                    .parent.get_text(strip=True)
                    .rstrip("P/E Ratio")
                    .replace(",", "")
                )
            except AttributeError:
                p_e = 100
            try:
                week_low = (
                    sp.find("div", string="52 Week Low")
                    .parent.get_text(strip=True)[:-11]
                    .replace(",", "")
                )
                week_high = (
                    sp.find("div", string="52 Week High")
                    .parent.get_text(strip=True)[:-11]
                    .replace(",", "")
                )
                potential_profit = round(float(week_high) * 100 / float(week_low))
            except AttributeError:
                potential_profit = 0

            name = sp.find(class_="price-section__label").get_text(strip=True)

            price = round(
                usd
                * float(
                    sp.find(class_="price-section__current-value")
                    .get_text()
                    .replace(",", "")
                ),
                2,
            )
            growth = float(
                soup.find(class_="table table-small")
                .select("td:nth-of-type(10)")[j]
                .find_all("span")[1]
                .get_text()
                .strip("%")
                .replace(",", "")
            )
            stocks.append(
                {
                    "code": company_code,
                    "name": name,
                    "price": price,
                    "P/E": p_e,
                    "growth": growth,
                    "potential profit": potential_profit,
                }
            )
    return stocks


def write_files(stocks):
    with open("top_ten_expensive_stocks", "w") as write_file:
        json.dump(
            sorted(stocks, key=lambda st: st.get("price"), reverse=True)[:10],
            write_file,
        )

    with open(
        "top_ten_stocks_with_lower_PE/home/nikita/PyStudy/homework11/Task2.py.json", "w"
    ) as write_file:
        json.dump(sorted(stocks, key=lambda st: st.get("P/E"))[:10], write_file)

    with open("top_ten_stocks_with_higher_growth.json", "w") as write_file:
        json.dump(
            sorted(stocks, key=lambda st: st.get("growth"), reverse=True)[:10],
            write_file,
        )

    with open("top_ten_stocks_with_potential_profit.json", "w") as write_file:
        json.dump(
            sorted(stocks, key=lambda st: st.get("potential profit"), reverse=True)[
                :10
            ],
            write_file,
        )
