class PeselLen:
    def __init__(self, pesel):
        self.pesel = pesel

    def pesel_len(self, pesel):
        if len(pesel) == 11:
            print("Len ERROR!")
            return 0


class ControlValue:
    def __init__(self, pesel):
        self.pesel = pesel

    def control_value(self):
        index = 0
        result = 0
        for x in self.pesel:
            if index == 0 or index == 4 or index == 8:
                result += (int(x) * 1) % 10
            if index == 1 or index == 5 or index == 9:
                result += (int(x)) * 3 % 10
            if index == 2 or index == 6:
                result += (int(x)) * 7 % 10
            if index == 3 or index == 7:
                result += (int(x) * 9) % 10
            index += 1

        result = result % 10
        control_nr = 10 - int(result)
        return control_nr


class Date:
    def __init__(self, pesel):
        self.pesel = str(pesel)
        pass

    def date_test(self, pesel):
        user_birthday = pesel[4:6]
        user_month = pesel[2:4]
        user_year = pesel[0:2]
        date = 0
        # 04260402376

        if int(user_birthday) > 31 and int(user_birthday) < 0:
            print("not valid day value")
            if int(user_month) > 12:
                print("not valid month value")
                return date + 2
        else:
            return date + 1


class GenderDec:
    def __init__(self, user_gender):
        self.user_gender = user_gender

    def gender_dec(self, user_gender):
        if int(user_gender) % 2 == 0 or int(user_gender) == 0:
            print("Gender : Female")
            return 1

        else:
            print("Gender : Male")
            return 1


def pesel_decoder(pesel):
    if not pesel.isdigit():
        quit("only numbers!")
    if len(pesel) != 11:
        quit("not the correct number of characters")

    user_gender = pesel[9]
    user_birthday = pesel[4:6]
    user_month = pesel[2:4]
    pesel_month = int(user_month)
    user_year = pesel[0:2]
    # 04260402376

    control_number = ControlValue(pesel)
    control_number.control_value()

    if control_number.control_value() != int(pesel[10]):
        print("the control number did not match")
        quit()

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

    if int(pesel_month) > 12:
        print("not valid month value")
        quit()

    offical_birthyear = str(century) + str(user_year)

    if len(pesel) == 11:
        print("\n")
        print("Birthday: %02d" % (int(user_birthday)))
        print("Month: %02d" % int(pesel_month))
        print("Year: ", str(offical_birthyear))
        print("Years old: ", 2021 - int(offical_birthyear))
        print(
            "Full date: %02d / %02d / %04s"
            % (int(user_birthday), int(pesel_month), str(offical_birthyear))
        )
        gender_pick = GenderDec(user_gender)
        gender_pick.gender_dec(user_gender)
        print("\n")
    else:
        print("pesel too short!")
