from playwright.sync_api import sync_playwright

def search_blinkit(query, location="122001"):
    results = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(f"https://www.blinkit.com/search?q={query}")

            page.wait_for_timeout(5000)  # Wait for content to load

            product_cards = page.locator("div.css-175oi2r")
            count = product_cards.count()
            for i in range(min(count, 5)):  # Limit results
                name = product_cards.nth(i).locator("p.Text__StyledText-sc-oo0kvp-0").nth(0).inner_text()
                price = product_cards.nth(i).locator("span.Text__StyledText-sc-oo0kvp-0").nth(1).inner_text()
                results.append({"name": name, "price": price})
            browser.close()
    except Exception as e:
        print("Blinkit Error:", e)
    return results
