from calculating import *
from peseldecoder import *
from peselgen import *
from click.testing import CliRunner
import pytest



@pytest.fixture(scope="module")
def runner():
    return CliRunner()

pesel = "13260282552"
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
    assert result.control_value() == 2

def test_male_gender_value():
    result = Gender(gender)
    man_numbers = [1, 3, 5, 7, 9]
    assert result.gender_value() in man_numbers

def test_female_gender_value():
    result = Gender(gender)
    woman_numbers = [0, 2, 4, 6, 8]
    assert result.gender_value() in woman_numbers

def test_leap_year():
    result = MonthCheck(2004, 2, 29)
    assert result.months_check() == 1

def test_click_generate():
    result = generate()
    assert generate == 1



# tests for DECODER
def test_gender_dec():
    result = GenderDec(4)
    assert result.gender_dec(4) == 1

def test_pesel_date():
    result = Date("")
    assert result.date_test(pesel) == 1

def test_cotrol_dec():
    result = ControlValue(pesel)
    assert result.control_value() == 2

def test_pesel_len():
    result = PeselLen(pesel)
    assert result.pesel_len(pesel) == 0

def test_leap_year_dec():
    result = MonthDec(2, 2008, 29)
    assert result.month_checker() == 1

#tests for Click

def test_for_decode_click(runner):
    result = runner.invoke(generate, ["2", "6", "2013", "male"])
    assert "your pesel number: " in result.output
    assert '132602' in result.output[21:27]

def test_for_gen_click(runner):
    result = runner.invoke(decode, ["13260282552"])
    assert "Birthday: 02" in result.output
    assert "Month: 06" in result.output
    assert "Year:  2013" in result.output
    assert "Years old:  8" in result.output
    assert "Full date: 02 / 06 / 2013" in result.output
    assert "Gender : Male" in result.output


