from calculating import Century
from calculating import Control
from calculating import Date
from calculating import Gender
from calculating import GenderDec
import pytest


####TESTS FOR GENERATOR
def test_century():
    result = Century(1)
    century = 20
    assert result.century_results(2050) == century

def test_control():
    result = Control("")
    assert result.control_index("04260402376") == 6

def test_pesel_len():
    pesel = "27926371917"
    assert len(pesel) == 11

def test_pesel_date():
    result = Date("")
    assert result.date_test("04260402376") == 1

def test_gender_value():
    result = Gender("")
    assert result.gender_value("male") == 1
    assert result.gender_value("female") == 1

def test_gender_dec():
    result = GenderDec(4)
    assert result.gender_dec(4) == 1














