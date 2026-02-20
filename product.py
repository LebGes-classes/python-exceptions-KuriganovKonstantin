class QuantityError(Exception):
    """Исключение для количества. """

    pass

class PriceError(Exception):
    """Исключение для цены. """

    pass

class WeightError(Exception):
    """Исключение для веса. """

    pass

class ProductCard:
    """Класс карточки товара."""

    def __init__(
            self,
            name: str = 'Неизвестно',
            quantity: int = 0,
            state: str = 'Не состоит на учёте',
            price: int = 0,
            weight: int = 0,
            product_id: str = '0000',
            description: str = 'Нет описания.',
            category: str = 'Неизвестно',
            colour: str = 'Не указан',
            country_of_origin: str = 'Неизвестно',
            brand: str = 'Без бренда.'
    ) -> None:
        """Инициализация/конструктор класса.

        Args:
            name: Наименование товара.
            quantity: Количество товара.
            state: Состояние товара.
            price: Стоимость товара.
            weight: Вес товара (в граммах).
            product_id: Идентификатор товара.
            description: Описание товара.
            category: Категория товара.
            colour: Цвет товара.
            country_of_origin: Страна производителя.
            brand: Бренд товара.
        """

        if quantity < 0:
            raise QuantityError(
                "Количество не может быть меньше нуля."
            )

        if price < 0:
            raise PriceError(
                "Стоимость не может быть меньше нуля."
            )

        if weight < 0:
            raise WeightError(
                "Вес не может быть меньше нуля."
            )

        self.__name = name
        self.__quantity = quantity
        self.__state = state
        self.__price = price
        self.__weight = weight
        self.__product_id = product_id
        self.__description = description
        self.__category = category
        self.__colour = colour
        self.__country_of_origin = country_of_origin
        self.__brand = brand

    def get_name(self) -> str:
        """Геттер для наименования товара.

        Returns:
            name: Наименование товара.
        """

        return self.__name

    def get_quantity(self) -> int:
        """Геттер для количества товара.

        Returns:
            quantity: Количество товара.
        """

        return self.__quantity

    def get_state(self) -> str:
        """Геттер для состояния товара.

        Returns:
            state: Состояние товара.
        """

        return self.__state

    def get_price(self) -> float:
        """Геттер для стоимости товара.

        Returns:
            price: Стоимость товара.
        """

        return self.__price

    def get_weight(self) -> float:
        """Геттер для веса товара.

        Returns:
            weight: Вес товара.
        """

        return self.__weight

    def get_product_id(self) -> str:
        """Геттер для идентификатора товара.

        Returns:
            product_id: Идентификатор товара.
        """

        return self.__product_id

    def get_description(self) -> str:
        """Геттер для описания товара.

        Returns:
            description: Описание товара.
        """

        return self.__description

    def get_category(self) -> str:
        """Геттер для категории товара.

        Returns:
            category: Категория товара.
        """

        return self.__category

    def get_colour(self) -> str:
        """Геттер для цвета товара.

        Returns:
            colour: Цвет товара.
        """

        return self.__colour

    def get_country_of_origin(self) -> str:
        """Геттер для страны производителя.

        Returns:
            country_of_origin: Страна производителя.
        """

        return self.__country_of_origin

    def get_brand(self) -> str:
        """Геттер для бренда товара.

        Returns:
            brand: Бренд товара.
        """
        return self.__brand

    def set_name(self, name: str) -> None:
        """Сеттер для наименования товара.

        Args:
            name: Наименование товара.
        """

        self.__name = name

    def set_quantity(self,quantity: int) -> None:
        """Сеттер для количества товара.

        Args:
            quantity: Количество товара.
        """

        if quantity < 0:
            raise ValueError("Количество товара не может быть меньше нуля.")

        self.__quantity = quantity

    def set_state(self, state: str) -> None:
        """Сеттер для состояния товара.

        Args:
            state: Состояние товара.
        """
        valid_states = ['принято к учёту', 'состоит на учёте',
                        'выявлена недостача', 'выявлен излишек', 'отказано в учёте']
        if state not in valid_states:
            raise ValueError("Некорректное состояние товара.")

        self.__state = state

    def set_price(self, price: float) -> None:
        """Сеттер для стоимости товара.

        Args:
            price: Стоимость товара.
        """

        if price < 0:
            raise ValueError("Стоимость товара не может быть меньше нуля.")

        self.__price = price

    def set_weight(self, weight: float) -> None:
        """Сеттер для веса товара.

        Args:
            weight: Вес товара.
        """

        if weight < 0:
            raise ValueError("Вес товара не может быть меньше нуля.")

        self.__weight = weight

    def set_product_id(self, product_id: str, product_ids: list[str]) -> None:
        """Сеттер для идентификатора товара.

        Args:
            product_id: Идентификатор товара.
            product_ids: Все идентификаторы.
        """
        if product_id in product_ids:
            raise ValueError("Идентификатор обязан быть уникальным.")

        if any(i not in '0123456789' for i in product_id):
            raise ValueError("Идентификатор должен состоять из цифр")

        product_ids.replace(self.__product_id, product_id)

        self.__product_id = product_id

    def set_description(self, description: str) -> None:
        """Сеттер для описания товара.

        Args:
            description: Описание товара.
        """

        self.__description = description

    def set_category(self, category: str) -> None:
        """Сеттер для категории товара.

        Args:
            category: Категория товара.
        """

        self.__category = category

    def set_colour(self, colour: str) -> None:
        """Сеттер для цвета товара.

        Args:
            colour: Цвет товара.
        """

        self.__colour = colour

    def set_country_of_origin(self, country: str) -> None:
        """Сеттер для страны производителя.

        Args:
            country: Страна производителя.
        """

        self.__country_of_origin = country

    def set_brand(self, brand: str) -> None:
        """Сеттер для бренда товара.

        Args:
            brand: Бренд товара.
        """

        self.__brand = brand

    def write_off(self) -> None:
        """Метод для списания карточки с учёта.
        Списание возможно только если состояние "принято к учёту"
        или "состоит на учёте".
        """

        valid_states = ["принято к учёту", "состоит на учёте"]

        if self.__state.lower() in valid_states:
            self.__state = "списано"
            self.__quantity = 0
            print(f"\nТовар '{self.__name}' успешно списан с учёта.")
        else:
            print(f"\nСписание невозможно. Текущее состояние: '{self.__state}'.")

    def display_info(self) -> None:
        """Вывод информации о товаре."""

        print(f' Наименование товара: {self.get_name()}')
        print(f' Количество товара: {self.get_quantity()}')
        print(f' Бренд товара: {self.get_brand()}')
        print(f' Стоимость товара: {self.get_price()}')
        print(f' Страна-производитель: {self.get_country_of_origin()}')
        print(f' Категория товара: {self.get_category()}')
        print(f' Описание товара: {self.get_description()}')
        print(f' Состояние товара: {self.get_state()}')
        print(f' Вес товара: {self.get_weight()}')
        print(f' Идентификатор товара: {self.get_product_id()}')
        print(f' Цвет товара: {self.get_colour()}')