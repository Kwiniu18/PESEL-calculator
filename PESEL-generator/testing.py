from calculating import Century
from calculating import Control
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









