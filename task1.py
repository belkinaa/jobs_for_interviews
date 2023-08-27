class Shares():
    SUMM_SHARES = 0
    NUMBER_OF_SHARES = []

    @classmethod
    def create_share(cls, share: float) -> None:
        """Создание доли:
            * запись значения
            * подсчет общей суммы"""
        cls.SUMM_SHARES += share
        cls.NUMBER_OF_SHARES.append(share)

    @classmethod
    def print_procent_share(cls) -> None:
        """Печатает процентное выражение каждой доли"""
        [print('%.3f' % round(i/cls.SUMM_SHARES, 3)) for i in cls.NUMBER_OF_SHARES]


[Shares().create_share(float(input())) for _ in range(int(input()))]
Shares.print_procent_share()



