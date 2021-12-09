import random
from datetime import date


class Control:
    def __init__(self, pesel):
        self.pesel = str(pesel)

    def control_value(self):
        result = 0

        for index, x in enumerate(self.pesel):
            if index == 0 or index == 4 or index == 8:
                result += (int(x)) * 1 % 10
            if index == 1 or index == 5 or index == 9:
                result += (int(x)) * 3 % 10
            if index == 2 or index == 6:
                result += (int(x)) * 7 % 10
            if index == 3 or index == 7:
                result += (int(x)) * 9 % 10
        result = result % 10
        control_value = 10 - int(result)

        if control_value == 10:
            control_value = 0
        pesel = str(self.pesel) + str(control_value)
        print("\n")
        print("your pesel number:", pesel)
        print("\n")
        return control_value


class Century:
    def __init__(self, year, month):
        self.year = year
        self.month = month


    def century_pick(self):

        if self.year < 1800 or self.year > 2299:
            raise ValueError("Wrong Year Value!")

        if self.year >= 1800 and self.year <= 1899:
            self.month = self.month + 80

        if self.year >= 1900 and self.year <= 1999:
            self.month = self.month

        if self.year >= 2000 and self.year <= 2099:
            self.month = self.month + 20

        if self.year >= 2100 and self.year <= 2199:
            self.month = self.month + 40

        if self.year >= 2200 and self.year <= 2299:
            self.month = self.month + 60
        return self.month


class Gender:
    def __init__(self, gender):
        self.gender = str(gender)

    def gender_value(self):

        man_numbers = [1, 3, 5, 7, 9]
        woman_numbers = [0, 2, 4, 6, 8]
        random_gender_value = random.randint(0, 4)

        if self.gender == "female":
            gender_number = woman_numbers[random_gender_value]
            return gender_number
        if self.gender == "male":
            gender_number = man_numbers[random_gender_value]
            return gender_number


class MonthCheck:
    def __init__(self, year, month, day):
        self.month = month
        self.year = year
        self.day = day

    def months_check(self):

        if self.month > 31 or self.month < 1:
            raise ValueError("Wrong Month Value")

        if self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                if self.day > 29:
                    raise ValueError("Wrong Month Value!")
            else:
                if self.day > 28:
                    raise ValueError("Wrong Month Value!")

        if self.month in [4, 6, 9, 11]:
            if self.day > 30:
                raise ValueError("Wrong month Value!")
        else:
            return 1
            pass


def pesel_gen(day, month, year, gender):

    pesel_year = year % 100
    pesel_day = day

    century = Century(year, month)
    century_month = century.century_pick()
    gender_pick = Gender(gender)

    month_check = MonthCheck(year, month, day)
    month_error = month_check.months_check()

    gender_number = gender_pick.gender_value()
    ordinal_nr = random.randint(0, 999)

    pesel = str(
        (
            "%02d%02d%02d%03d%01d"
            % (
                pesel_year,
                century_month,
                pesel_day,
                ordinal_nr,
                gender_number,
            )
        )
    )

    # GENERATING CONTROL VALUE

    control = Control(pesel)
    control.control_value()
