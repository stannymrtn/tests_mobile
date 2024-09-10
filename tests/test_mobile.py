import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.tag("mobile")
@allure.label("owner", "Timur")
@allure.feature("Пример теста для мобильных устройств")
@allure.story("Поиск на сайте")
def test_search():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

@allure.tag("mobile")
@allure.label("owner", "Игорь Трубихов")
@allure.feature("Википедия_примеры тесов для мобильных устройств")
@allure.story("Открытие результата поиска")
def test_open_first_article():
    with allure.step('Type search "Java"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Python')

    with allure.step('Verify content found.'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Python'))

    with allure.step('Click the first article.'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()