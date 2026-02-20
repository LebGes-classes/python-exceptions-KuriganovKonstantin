from product import*


def display() -> None:
    """Вывод меню."""

    print("\n----------- МЕНЮ ВЗАИМОДЕЙСТВИЯ -------------"
          "\n1. Создать карточку товара."
          "\n2. Показать карточку товара."
          "\n3. Изменить данные карточки."
          "\n4. Списать карточку товара."
          "\n5. Удалить карточку товара."
          "\n6. Показать все карточки товаров."
          "\n0.Выход из программы."
          "\n------------------------------------------------"
          )


def check_for_emptiness(input_word: str) -> str:
    """Проверка, пустой ли ввод.

    Args:
        input_word: Ввод.

    Returns:
        input_word: Ввод.
    """

    while True:
        try:
            if input_word == '':
                raise ValueError("Вы ничего не ввели.")
            else:
                return input_word
        except ValueError as ve:
            print(ve)

            input_word = input("Попробуйте снова: ")


def check_for_int(input_word: str) -> int:
    """Проверка на число.

    Args:
        input_word: Ввод.

    Returns:
        input_word: Ввод.
    """

    input_word = check_for_emptiness(input_word)

    while True:
        try:
            if any(i not in '-0123456789' for i in input_word):
                raise TypeError("Должно было быть введено число.")
            else:
                return int(input_word)
        except TypeError as te:
            print(te)

            input_word = check_for_emptiness(input("Попробуйте снова: "))


class Menu:
    """Класс меню."""

    def __init__(self, products: list[ProductCard]) -> None:
        """Инициализация класса Menu.

        Args:
            products: Экземпляр класса product.
        """

        self.products = products
        self.current_ids = [product.get_product_id() for product in products]

    def main_menu(self) -> None:
        """Основная часть меню."""

        is_running = True

        while is_running:
            while True:
                display()

                choice = check_for_int(input("Выберите действие: "))

                try:
                    match int(choice):
                        case 1:
                            name = check_for_emptiness(input("Введите наименование: "))
                            quantity = check_for_int(input("Введите количество: "))
                            state = check_for_emptiness(input("Введите состояние (напр. 'В наличии'): "))
                            price = check_for_int(input("Введите цену: "))
                            weight = check_for_int(input("Введите вес (в граммах): "))
                            product_id = check_for_emptiness(input("Введите идентификатор (ID): "))
                            description = check_for_emptiness(input("Введите описание: "))
                            category = check_for_emptiness(input("Введите категорию: "))
                            colour = check_for_emptiness(input("Введите цвет: "))
                            country = check_for_emptiness(input("Введите страну-производитель: "))
                            brand = check_for_emptiness(input("Введите бренд: "))

                            self.current_ids.append(product_id)
                            while True:
                                try:
                                    new_card = ProductCard(
                                        name, quantity, state, price, weight,
                                        product_id, description, category, colour,
                                        country, brand
                                    )

                                    self.products.append(new_card)
                                except QuantityError as qe:
                                    print(qe)

                                    quantity = check_for_int(input("Введите количество: "))
                                except PriceError as pe:
                                    print(pe)

                                    price = check_for_int(input("Введите цену: "))
                                except WeightError as we:
                                    print(we)

                                    weight = check_for_int(input("Введите вес (в граммах): "))
                                else:
                                    break

                        case 2:
                            choice_of_product = check_for_int(input("Выберите товар: "))

                            self.products[choice_of_product - 1].display_info()

                        case 3:
                            choice_of_product = check_for_int(input("Выберите товар: "))

                            print("\n---------- Что вы хотите изменить? -------------"
                                  "\n1. Наименование"
                                  "\n2. Количество"
                                  "\n3. Состояние"
                                  "\n4. Цена"
                                  "\n5. Вес"
                                  "\n6. Категория"
                                  "\n7. Цвет"
                                  "\n8. Страна-производитель"
                                  "\n9. Бренд"
                                  "\n10.Идентификатор"
                                  "\n11.Описание"
                                  "\n------------------------------------------------"
                                  )

                            choice = check_for_int(input("Выберите товар: "))

                            match choice:
                                case 1:
                                    new_name = check_for_emptiness(input("Введите новое наименование: "))

                                    self.products[choice_of_product - 1].set_name(new_name)
                                case 2:
                                    while True:
                                        try:
                                            new_quantity = check_for_int(input("Введите новое количество: "))

                                            self.products[choice_of_product - 1].set_quantity(new_quantity)
                                        except ValueError:
                                            print(ValueError)
                                        else:
                                            break
                                case 3:
                                    while True:
                                        try:
                                            new_state = check_for_emptiness(input("Введите новое состояние: "))

                                            self.products[choice_of_product - 1].set_state(new_status)
                                        except ValueError:
                                            print(ValueError)
                                        else:
                                            break
                                case 4:
                                    while True:
                                        try:
                                            new_price = check_for_int(input("Введите новую цену: "))

                                            self.products[choice_of_product - 1].set_price(new_price)
                                        except ValueError:
                                            print(ValueError)
                                        else:
                                            break
                                case 5:
                                    while True:
                                        try:
                                            new_weight = check_for_int(input("Введите новый вес: "))

                                            self.products[choice_of_product - 1].set_weight(new_weight)
                                        except ValueError:
                                            print(ValueError)
                                        else:
                                            break
                                case 6:
                                    new_category = check_for_emptiness(input("Введите новую категорию: "))

                                    self.products[choice_of_product - 1].set_category(new_category)
                                case 7:
                                    new_color = check_for_emptiness(input("Введите новый цвет: "))

                                    self.products[choice_of_product - 1].set_colour(new_color)
                                case 8:
                                    new_country = check_for_emptiness(input("Введите новую страну-производитель: "))

                                    self.products[choice_of_product - 1].set_country_of_origin(new_country)
                                case 9:
                                    new_brand = check_for_emptiness(input("Введите новый бренд: "))

                                    self.products[choice_of_product - 1].set_brand(new_brand)
                                case 10:
                                    while True:
                                        try:
                                            new_id = check_for_emptiness(input("Введите новый идентификатор: "))

                                            self.products[choice_of_product - 1].set_product_id(new_id, self.current_ids)
                                        except ValueError:
                                            print(ValueError)
                                        else:
                                            break
                                case 11:
                                    new_description = check_for_emptiness(input("Введите новое описание: "))

                                    self.products[choice_of_product - 1].set_description(new_description)
                                case _:
                                    raise ValueError("Неверный выбор.")

                            print("Успешная замена!!!")

                        case 4:
                            choice_of_product = check_for_int(input("Выберите товар: "))

                            self.products[choice_of_product - 1].write_off()

                        case 5:
                            choice_of_product = check_for_int(input("Выберите товар: "))

                            del self.products[choice_of_product - 1]

                        case 6:
                            i = 0
                            for product in self.products:
                                i += 1

                                print(f"Вывод информации о товаре №{i}")
                                print('_______________________________')
                                product.display_info()
                                print('_______________________________')

                        case 0:
                            is_running = False

                        case _:
                            raise ValueError("Неверный выбор.")
                except ValueError:
                    print(ValueError)
                else:
                    break







