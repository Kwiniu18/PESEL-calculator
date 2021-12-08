import random


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


def pesel_gen(day, month, year, gender):

    pesel_year = year % 100
    pesel_day = day
    century = Century(year, month)
    month = century.century_pick()
    gender_pick = Gender(gender)
    gender_number = gender_pick.gender_value()

    pesel = str(
        (
            "%02d%02d%02d%03d%01d"
            % (
                pesel_year,
                month,
                pesel_day,
                random.randint(0, 999),
                gender_number,
            )
        )
    )

    # GENERATING CONTROL VALUE

    control = Control(pesel)
    control.control_value()
