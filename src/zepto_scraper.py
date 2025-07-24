from playwright.sync_api import sync_playwright

def search_zepto(product, location):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("https://www.zeptonow.com/", timeout=60000)
            page.fill("input[placeholder='Enter delivery location']", location)
            page.keyboard.press("Enter")
            page.wait_for_timeout(3000)

            search_box = page.wait_for_selector("input[placeholder='Search for products']", timeout=10000)
            search_box.fill(product)
            page.keyboard.press("Enter")
            page.wait_for_timeout(3000)

            items = page.query_selector_all("div.ProductCard")
            results = []
            for item in items:
                name = item.query_selector("div.ProductCard__Name").inner_text()
                price = item.query_selector("div.ProductCard__Price").inner_text()
                results.append({"name": name, "price": price})

            return results
        except Exception as e:
            return []
        finally:
            browser.close()
