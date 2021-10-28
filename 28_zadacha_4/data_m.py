class Date:

    def __init__(self, date, month, year, allow=False):
        if not allow:
            raise TypeError('Нельзя инициализировать обьекты этого класса таким образом')
        else:
            self.__date = date
            self.__month = month
            self.__year = year

    @staticmethod
    def from_string(some_string):
        data = some_string.split('-')
        if len(data) != 3:
            raise ValueError('Пример ввода даты: 10-12-2077')
        else:
            a = Date(date=int(data[0]), month=int(data[1]), year=int(data[2]), allow=True)
            return a

    @staticmethod
    def is_date_valid(some_string):
        data = some_string.split('-')
        if len(data) != 3:
            return False
        if 0 < int(data[0]) < 31 and 0 < int(data[1]) < 13 and int(data[2]) > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"День: {self.__date} Месяц: {self.__month} Год: {self.__year}"
