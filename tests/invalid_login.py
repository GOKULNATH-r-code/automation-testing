from playwright.sync_api import sync_playwright

with sync_playwright() as p :

    browser =  p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("invalidName")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    page.screenshot(path="test-results/invaild-login.png")
    page.wait_for_timeout(3000)
    browser.close()