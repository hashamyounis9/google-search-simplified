from flask import Flask, request, jsonify
import nodriver as uc
from bs4 import BeautifulSoup
import asyncio


app = Flask(__name__)


async def scrape(q):
    browser = await uc.start(headless=True)
    page = await browser.get(f"https://google.com/search?q={q}")
    await page.scroll_down(75)
    await page.sleep(2)
    await page.wait_for(selector='#botstuff > div > div:nth-child(3)', timeout=3)

    titles = []
    try:
        # global title
        titles = await page.select_all('h3')
    except:
        return {"error": "Some error occured while performing query",
                "hint": "Maybe your query is invalid/unclear"}

    elements = await page.select_all('.N54PNb.BToiNc.cvP2Ce')
    searche_results = elements

    results = []
    i = 1
    for result in searche_results:
        search = {}
        soap = BeautifulSoup(await result.get_html(), 'html.parser')

        anchor = soap.find('a')
        search['site_url'] = anchor.get('href') if anchor else None

        title = soap.find("h3")
        search['result_heading'] = title.text.strip() if title else None

        site_name = soap.find(class_="VuuXrf")
        search['result_by_site'] = site_name.text.strip() if site_name else None

        overview = soap.find(class_="VwiC3b yXK7lf lVm3ye r025kc hJNv6b Hdw6tb")
        search['result_overview'] = overview.text.strip() if overview else None

        img = soap.find('img')
        search['site_logo'] = img.get('src') if img else None

        results.append(search)
    browser.stop()
    return results


@app.route('/')
def index():
    q = request.args.get('q')
    if not q:
        return jsonify({"Error": "q (argument to send query to api) is missing...",
                        "Suggestion": "Try again :)",
                        "Usage": "https://api_url/?q={your_query}"})
    else:
        result = uc.loop().run_until_complete(scrape(q))
        return jsonify(result)
    return jsonify({"Error": "some unknown error occured..."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
