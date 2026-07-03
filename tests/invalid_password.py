from playwright.sync_api import sync_playwright , expect

with sync_playwright() as p :
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("student")
    page.locator("#password").fill("invalidPassword")
    page.locator("#submit").click()
    expect(page.get_by_text("Your password is invalid!"))
    page.screenshot(path="test-results/invalid_password.png")
    # path="test-results/invaild-login.png"
    page.wait_for_timeout(3000)
    browser.close()