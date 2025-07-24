from playwright.sync_api import sync_playwright

def search_blinkit(product, location):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("https://www.blinkit.com/", timeout=60000)
            page.fill("input[placeholder='Enter your area or pincode']", location)
            page.click("text=Continue")
            page.wait_for_timeout(3000)

            search_box = page.wait_for_selector("input[type='search']", timeout=10000)
            search_box.fill(product)
            page.keyboard.press("Enter")
            page.wait_for_timeout(3000)

            items = page.query_selector_all("div.ProductCard__Details")
            results = []
            for item in items:
                name = item.query_selector("div.ProductCard__Title").inner_text()
                price = item.query_selector("div.ProductCard__Price").inner_text()
                results.append({"name": name, "price": price})

            return results
        except Exception as e:
            return []
        finally:
            browser.close()
