import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    @allure.step('Инициализация страницы. Открытие URL: {url}')
    def __init__(self, driver, url, time=10):
        """
        Инициализация базовой страницы.
        :param driver: Экземпляр веб-драйвера.
        :param url: URL страницы для открытия.
        :param time: Время ожидания по умолчанию (по умолчанию 10 секунд).
        """
        self.driver = driver
        self.driver.get(url)
        self.time = time

    @allure.step('Открываем страницу по URL')
    def open_page(self, url):
        """ Открываем страницу по URL {page_url} """
        return self.driver.get(url)

    @allure.step('Поиск элемента по локатору: {locator}')
    def find_element(self, locator, time=20):
        """
        Поиск элемента на странице с ожиданием его видимости.
        :param locator: Локатор элемента.
        :param time: Время ожидания (по умолчанию 10 секунд).
        :return: Найденный элемент.
        """
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f'Не удалось найти элемент {locator}'
        )

    def wait_for_load_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Ждем загрузку всех элементов HTML по локатору')
    def wait_for_load_all_elements(self, locator):
        """ Ждем загрузку всех элементов HTML по локатору {locator} """
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(locator))

    @allure.step('Клик по элементу с локатором: {locator}')
    def click(self, locator, time=10):
        """
        Клик по элементу с ожиданием его кликабельности.
        :param locator: Локатор элемента.
        :param time: Время ожидания (по умолчанию 10 секунд).
        """
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f'Элемент {locator} не кликабелен'
        ).click()

    @allure.step('Ввод текста "{text}" в элемент с локатором: {locator}')
    def add_text_into_element(self, locator, text):
        """
        Ввод текста в элемент.
        :param locator: Локатор элемента.
        :param text: Текст для ввода.
        """
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текста из элемента с локатором: {locator}')
    def get_text(self, locator, time=10):
        """
        Получение текста из элемента с ожиданием его видимости.
        :param locator: Локатор элемента.
        :param time: Время ожидания (по умолчанию 10 секунд).
        :return: Текст элемента.
        """
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f'Элемент {locator} не виден'
        ).text

    @allure.step('Ожидание исчезновения элемента с локатором: {locator}')
    def element_invisibility(self, locator):
        """
        Ожидание исчезновения элемента.
        :param locator: Локатор элемента.
        """
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator),
            message=f'Элемент {locator} отображается, хотя не должен'
        )

    @allure.step('Перемещение элемента из {source_locator} в {new_locator}')
    def moving_element(self, source_locator, new_locator):
        """
        Перемещение элемента из одного места в другое.
        :param source_locator: Локатор исходного элемента.
        :param new_locator: Локатор целевого элемента.
        """
        source = self.driver.find_element(*source_locator)
        destination = self.driver.find_element(*new_locator)
        ActionChains(self.driver).click_and_hold(source).move_to_element(destination).release().perform()

    def wait_for_changed_text(self, locator, value):
        """
        Ожидание, пока текст элемента перестанет быть равным определённому значению.
        :param locator: Локатор элемента.
        :param value: Значение текста, которое должно измениться.
        :return: True, если текст изменился, иначе False.
        """
        try:
            WebDriverWait(self.driver, 20).until_not(
                EC.text_to_be_present_in_element(locator, value))
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Проверка кликабельности элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.step('Нажатие на элемент')
    def click_on_element(self, locator):
        target = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Проверка отображения элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element_with_wait(*locator).is_displayed()

    @allure.step('Поиск элемента на странице')
    def find_element_with_wait(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Получение текста на элементе')
    def get_text_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text




