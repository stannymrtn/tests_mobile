import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure_commons._allure import step


@allure.tag("Mobile")
@allure.label("owner", "Timur")
@allure.feature("Пример теста для мобильных устройств")
@allure.story("Поиск на сайте")
def test_search():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.tag("Mobile")
@allure.label("owner", "Timur")
@allure.feature("Пример теста для мобильных устройств")
@allure.story("Открытие результата поиска")
def test_open_first_article():
    with step('Type search "Python"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Python')

    with step('Verify content found.'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Python'))

    with step('Click the first article.'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()
