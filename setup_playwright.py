import asyncio
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Just trigger browser install
        browser = p.chromium.launch()
        browser.close()

if __name__ == "__main__":
    run()
