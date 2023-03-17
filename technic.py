class Technic:
    """
    Класс описывающий товар
    """

    def __init__(self, name: str, price: int, is_in_stock: bool = True) -> None:
        self.name = name
        self.price = price
        self.is_in_stock = is_in_stock

        if self.price >= 1000:
            self.category = "Дорогой"
        else:
            self.category = "Бюджетный"

    def get_category(self):
        return self.category

    def __setattr__(self, key, value):
        if key in ['name', 'price', 'is_in_stock', 'category']:
            super().__setattr__(key, value)
        return "ERROR"

    def __repr__(self):
        return self.name


test_1 = Technic(name="tovar_111", price=1999, is_in_stock=True)
test_2 = Technic(name="tovar_12", price=999, is_in_stock=True)


# сравнение длинн названий техники
# def names_comparing(name_1, name_2):
#     if len(name_1) > len(name_2):
#         return "Первое имя длиннее"
#     return "Второе имя длиннее"
#
#
# print(names_comparing(test_1.name, test_2.name))

# print(len(test_1.name).__eq__(len(test_2.name)))
# print(len(test_1.name).__gt__(len(test_2.name)))
# print(len(test_1.name).__le__(len(test_2.name)))
# print(len(test_1.name).__ge__(len(test_2.name)))
