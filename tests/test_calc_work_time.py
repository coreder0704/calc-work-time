from calc_work_time import main
from datetime import timedelta
import pytest


def test_translate_timeformat():
    assert main.translate_timeformat("8:45") == timedelta(hours=8, minutes=45)
    assert main.translate_timeformat("25:00") == timedelta(hours=25)
    with pytest.raises(SystemExit, match="Error: Non-numeric string for time."):
        main.translate_timeformat("foo")


def test_calc_overtime():
    assert main.calc_overtime("9:00", "17:30") == "0:15"
