from playwright.sync_api import sync_playwright

def search_zepto(query, location="122001"):
    results = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(f"https://www.zeptonow.com/search?q={query}")

            page.wait_for_timeout(5000)

            product_cards = page.locator("div.ProductCard__Container")
            count = product_cards.count()
            for i in range(min(count, 5)):
                name = product_cards.nth(i).locator("h2").inner_text()
                price = product_cards.nth(i).locator("span").nth(1).inner_text()
                results.append({"name": name, "price": price})
            browser.close()
    except Exception as e:
        print("Zepto Error:", e)
    return results
