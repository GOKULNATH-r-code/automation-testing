from playwright.sync_api import sync_playwright , expect

with sync_playwright() as p :
    browser =  p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/logged-in-successfully/")

    page.get_by_role("link", name="Log out").click()
    page.screenshot(path="test-results/logout.png")
    page.wait_for_timeout(300)
    browser.close()