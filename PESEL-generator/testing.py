from calculating import Century
from calculating import Control
from peseldecoder import Date
from calculating import Gender
from peseldecoder import GenderDec
from peseldecoder import ControlValue
from peseldecoder import PeselLen
import pytest

pesel = "04260402376"
year = 2004
month = 10
century = 30
gender = "male"

####TESTS FOR GENERATOR
def test_century():
    result = Century(year, month)
    assert result.century_pick() == century


def test_control():
    result = Control(pesel)
    assert result.control_value() == 6


def test_gender_value():
    result = Gender(gender)
    man_numbers = [1, 3, 5, 7, 9]
    woman_numbers = [0, 2, 4, 6, 8]
    assert result.gender_value() in man_numbers


# DECODER
def test_gender_dec():
    result = GenderDec(4)
    assert result.gender_dec(4) == 1


def test_pesel_date():
    result = Date("")
    assert result.date_test(pesel) == 1


def test_cotrol_dec():
    result = ControlValue(pesel)
    assert result.control_value() == 6


def test_pesel_len():
    result = PeselLen(pesel)
    assert result.pesel_len(pesel) == 0
