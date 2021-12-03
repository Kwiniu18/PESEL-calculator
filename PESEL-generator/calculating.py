import random



######################################################################################
######################################################################################
#############################    PESEL GENERATOR       ###############################
######################################################################################
######################################################################################




def pesel_gen(day, month, year, gender):
    pesel_year = year % 100
    pesel_day = day


    if year >= 1800 and year <= 1899:
        pesel_month = month + 80

    if year >= 1900 and year <= 1999:
        pesel_month = month

    if year >= 2000 and year <= 2099:
        pesel_month = month + 20

    if year >= 2100 and year <= 2199:
        pesel_month = month + 40

    if year >= 2200 and year <= 2299:
        pesel_month = month + 60

        # GENERATING ORDINAL NUMBER
    ordinal_number = random.randint(0, 999)

    man_numbers = [1, 3, 5, 7, 9]
    woman_numbers = [0, 2, 4, 6, 8]
    random_gender_value = random.randint(0, 4)

    if gender == "female":
        gender_number = woman_numbers[random_gender_value]
    if gender == "male":
        gender_number = man_numbers[random_gender_value]

    pesel = str(
        (
            "%02d%02d%02d%03d%01d"
            % (pesel_year, pesel_month, pesel_day, ordinal_number, gender_number)
        )
    )

    # GENERATING CONTROL VALUE
    index = 0
    result = 0

    for x in pesel:
        if index == 0 or index == 4 or index == 8:
            result += (int(x)) * 1 % 10
        if index == 1 or index == 5 or index == 9:
            result += (int(x)) * 3 % 10
        if index == 2 or index == 6:
            result += (int(x)) * 7 % 10
        if index == 3 or index == 7:
            result += (int(x)) * 9 % 10
        index += 1
    result = result % 10
    control_value = 10 - int(result)
    if control_value == 10:
        control_value = 0
    # print(control_value)

    pesel = str(pesel) + str(control_value)
    print("\n")
    print("your pesel number:", pesel)
    print("\n")



######################################################################################
######################################################################################
############################        PESEL DECODER       ##############################
######################################################################################
######################################################################################

def pesel_decoder(pesel):

    user_gender = pesel[9]
    user_birthday = pesel[4:6]
    user_month = pesel[2:4]
    pesel_month = int(user_month)
    user_year = pesel[0:2]
    century = 0
    #04260402376

    if int(user_birthday) > 31:
        print("not valid day value")
        quit()
    if int(user_month) > 12:
        print("not valid month value")
        quit()

    index = 0
    result = 0
    for x in pesel:
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
    control_value = 10 - int(result)
    # print(control_value)
    # print(pesel[10])


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

    offical_birthyear = str(century) + str(user_year)
    if int(offical_birthyear) < 1800 or int(user_year) > 2299:
        print("not valid year value")
        quit()


    if len(pesel) == 11:
        print("\n")
        print("Birthday: %02d" % (int(user_birthday)))
        print("Month: %02d" % int(pesel_month))
        print("Year: ", str(offical_birthyear))
        print("Years old: ", 2021 - int(offical_birthyear))
        print("Full date: %02d / %02d / %04s" % (int(user_birthday), int(pesel_month), str(offical_birthyear)))
        if int(user_gender) % 2 == 0 or int(user_gender) == 0:
            print("Gender: Female")
            print("\n")
        else:
            print("Gender : Male")
            print("\n")
    else:
        print("pesel too short!")


######################################################################################
######################################################################################
#############################     FOR TESTING    #####################################
######################################################################################
######################################################################################


class Century:
    def __init__(self, year):
        self.year = year


    def century_results(self, year):

        if year >= 1800 and year <= 1899:
            return 80

        if year >= 1900 and year <= 1999:
            return 0

        if year >= 2000 and year <= 2099:
            return 20

        if year >= 2100 and year <= 2199:
            return 40

        if year >= 2200 and year <= 2299:
            return 60


class Control:
    def __init__(self, pesel):
        self.pesel = str(pesel)

    def control_index(self, pesel):
        index = 0
        result = 0

        for x in pesel:
            if index == 0 or index == 4 or index == 8:
                result += (int(x)) * 1 % 10
            if index == 1 or index == 5 or index == 9:
                result += (int(x)) * 3 % 10
            if index == 2 or index == 6:
                result += (int(x)) * 7 % 10
            if index == 3 or index == 7:
                result += (int(x)) * 9 % 10
            index += 1
        result = result % 10
        control_value = 10 - int(result)
        if control_value == 10:
            control_value = 0
        return control_value

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

class Gender:
    def __init__(self, gender):
        self.gender = str(gender)

    def gender_value(self, gender):
        ordinal_number = random.randint(0, 999)

        man_numbers = [1, 3, 5, 7, 9]
        woman_numbers = [0, 2, 4, 6, 8]
        random_gender_value = random.randint(0, 4)

        if gender == "female":
            gender_number = woman_numbers[random_gender_value]
            return 1
        if gender == "male":
            gender_number = man_numbers[random_gender_value]
            return 1
        if gender not in ["male", "female"]:
            return 2

class GenderDec:
    def __init__(self, user_gender):
        self.user_gender = user_gender

    def gender_dec(self, user_gender):
        if int(user_gender) % 2 == 0 or int(user_gender) == 0:
            return 1

        else:
            print("Gender : Male")
            return 1
