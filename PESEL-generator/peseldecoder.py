from datetime import date
today = date.today()

    #pesel lenght validation
class PeselLen:
    def __init__(self, pesel):
        self.pesel = pesel

    def pesel_len(self, pesel):
        if len(pesel) == 11:
            print("Len ERROR!")
            return True

    #calculating control value
class ControlValue:
    def __init__(self, pesel):
        self.pesel = pesel

    def control_value(self):
        result = 0
        for index, x in enumerate(self.pesel):
            if index == 0 or index == 4 or index == 8:
                result += (int(x) * 1) % 10
            if index == 1 or index == 5 or index == 9:
                result += (int(x)) * 3 % 10
            if index == 2 or index == 6:
                result += (int(x)) * 7 % 10
            if index == 3 or index == 7:
                result += (int(x) * 9) % 10

        result = result % 10
        control_nr = 10 - int(result)
        if control_nr == 10:
            control_nr = 0
        return control_nr


    #Date validation
class Date:
    def __init__(self, pesel):
        self.pesel = str(pesel)
        pass

    def date_test(self, pesel):
        user_birthday = pesel[4:6]
        user_month = pesel[2:4]
        user_year = pesel[0:2]

        if int(user_birthday) > 31 or int(user_birthday) < 0:
            print("not valid day value")
            if int(user_month) > 12:
                print("not valid month value")
                return False
        else:
            return True

    #gender validation
class GenderDec:
    def __init__(self, user_gender):
        self.user_gender = user_gender

    def gender_dec(self, user_gender):
        if int(user_gender) % 2 == 0 or int(user_gender) == 0:
            print("Gender : Female")
            return True

        else:
            print("Gender : Male")
            return True

    #Month Validation
class MonthDec:
    def __init__(self, pesel_month, offical_birthyear, user_birthday):

        self.pesel_month = pesel_month
        self.offical_birthyear = offical_birthyear
        self.user_birthday = user_birthday

    def month_checker(self):

        if int(self.pesel_month) == 2:

            if int(self.offical_birthyear) % 4 == 0 and (
                    int(self.offical_birthyear) % 100 != 0 or int(self.offical_birthyear) % 400 == 0):
                if int(self.user_birthday) > 29:
                    raise ValueError("Wrong Month Value!")
            else:
                if int(self.user_birthday) > 28:
                    raise ValueError("Wrong Month Value!")

        if int(self.pesel_month) in [4, 6, 9, 11]:
            if int(self.user_birthday) > 30:
                raise ValueError("Wrong month Value!")
        else:
            return True


def pesel_decoder(pesel):
    if not pesel.isdigit():
        raise ValueError("only numbers!")
    if len(pesel) != 11:
        raise ValueError("not the correct number of characters")


    user_gender = pesel[9]
    user_birthday = pesel[4:6]
    user_month = pesel[2:4]
    pesel_month = int(user_month)
    user_year = pesel[0:2]


    control_number = ControlValue(pesel)
    control_number.control_value()

    #century validation

    if control_number.control_value() != int(pesel[10]):
        raise ValueError("Control number Wrong!")

    if int(user_month) > 12 and int(user_month) < 41:
        pesel_month = int(user_month) - 20
        century = 20
    if int(user_month) > 32 and int(user_month) < 61:
        pesel_month = int(user_month) - 40
        century = 21
    if int(user_month) > 52 and int(user_month) < 72:
        pesel_month = int(user_month) - 60
        century = 22
    if int(user_month) > 80 and int(user_month) < 93:
        pesel_month = int(user_month) - 80
        century = 18
    if int(user_month) > 0 and int(user_month) < 13:
        pesel_month = int(user_month)
        century = 19

    date = Date(pesel)
    date.date_test(pesel)

    #day and month validation

    if int(pesel_month) > 12 or int(pesel_month) < 1:
        raise ValueError("Wrong month value!")

    if int(user_birthday) > 31 or int(user_birthday) < 1:
        raise ValueError("Wrong Month Value")



    offical_birthyear = str(century) + str(user_year)

    years = today.year - int(offical_birthyear)

    # CALCULATING USER AGE
    if today.month >= int(pesel_month):
        if today.day < int(user_birthday):
            years = years - 1


    month_check = MonthDec(offical_birthyear, user_birthday, pesel_month)
    month_check.month_checker()


    if len(pesel) == 11:
        print("\n")
        print("Birthday: %02d" % (int(user_birthday)))
        print("Month: %02d" % int(pesel_month))
        print("Year: ", str(offical_birthyear))
        print("Years old: ", years)
        print(
            "Full date: %02d / %02d / %04s"
            % (int(user_birthday), int(pesel_month), str(offical_birthyear))
        )
        gender_pick = GenderDec(user_gender)
        gender_pick.gender_dec(user_gender)
        print("\n")

