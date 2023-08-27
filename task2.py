class Bonds():
    def __init__(self, information: str):
        self.day, self.name, self.price, self.cupons = information.split()
        self.day = int(self.day)
        self.price = float(self.price)
        self.cupons = int(self.cupons)


class Traiders():
    def __init__(self, information: str):
        self.day, self.number_of_lots, self.amount_of_money = map(int, information.split())
        self.MEMORY_BONDS = {}

    def set_inform_bonds(self):
        """Группируем по кампании, чтобы делать покупку не у одной кампании"""
        while (input_inform := input()):
            Bond = Bonds(input_inform)
            if Bond.name in self.MEMORY_BONDS:
                self.MEMORY_BONDS[Bond.name].append({'price': Bond.price,
                                                     'day': Bond.day,
                                                     'cupons': Bond.cupons,
                                                     'name': Bond.name})
            else:
                self.MEMORY_BONDS[Bond.name] = [{'price': Bond.price,
                                                 'day': Bond.day,
                                                 'cupons': Bond.cupons,
                                                 'name': Bond.name}]

    def get_max_bonds(self) -> list:
        """Возвращает отсортированный список словарей по цене"""
        table_memory = []
        for name_bond, list_bond in self.MEMORY_BONDS.items():
            sorted_list_bond = sorted(list_bond, key=lambda dict_bond: dict_bond['price'], reverse=True)
            table_memory.append(sorted_list_bond)

        table_memory = sorted(table_memory, key=lambda l_data: l_data[0]['price'], reverse=True)
        return table_memory


    def get_count_pay_bond(self, bond: dict) -> int:
        """Получаем количесвто купленных лотов"""
        price = bond.get('price') * 10
        if (count_pay := self.amount_of_money // price) == 0:
            return 0
        while count_pay > bond.get('cupons'):
            count_pay -= 1
        self.amount_of_money -= count_pay * price
        return int(count_pay)

    def payment(self, step_pay: int = 0):
        """step_pay - заготовка для шага покупки(В качестве усовершенстования в будущем).
        В условии ничего не написано, что делать если после максимальных покупок
        Остались деньги. Как вариант можно пробежаться по 2 кругу и купить дублирующих акций кампаний.
        """
        memory = []
        for bond in self.get_max_bonds():
            memory.append({
                'day': bond[step_pay].get('day'),
                'name': bond[step_pay].get('name'),
                'price': bond[step_pay].get('price'),
                'count': self.get_count_pay_bond(bond[step_pay])
            })
        return memory


    def print_income(self):
        income = 0
        if (is_payment := Traider.payment()):
            for item_payment in is_payment:
                price_full = item_payment.get('price') * 10 * item_payment.get("count")
                price_nominal = price_full // 1000
                consumption = price_full % 1000
                income += (price_nominal * 30 - consumption)
        print(income)
        [print(f'{item.get("day")} {item.get("name")} {item.get("price")} {item.get("count")}') for item in is_payment]




Traider = Traiders(input())
Traider.set_inform_bonds()
Traider.print_income()

