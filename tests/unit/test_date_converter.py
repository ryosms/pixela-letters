from datetime import datetime

from pixela_letters.date_converter import parse_from_ymd_string, find_last_start_date, convert_to_ymd_string


def test_can_parse_valid_date():
    result = parse_from_ymd_string('20181112')
    assert result is not None


def test_cannot_parse_invalid_date():
    result = parse_from_ymd_string('20181131')
    assert result is None


def test_cannot_parse_invalid_string():
    result = parse_from_ymd_string('abc')
    assert result is None


def test_can_convert_to_string():
    actual = convert_to_ymd_string(datetime(year=2018, month=11, day=12))
    expected = '20181112'
    assert actual == expected


def test_can_find_last_start_date():
    target = datetime(year=2018, month=11, day=12)
    expected = datetime(year=2018, month=11, day=11)
    actual = find_last_start_date(target)
    assert actual == expected


def test_can_find_last_start_date2():
    target = datetime(year=2018, month=12, day=1)
    expected = datetime(year=2018, month=11, day=25)
    actual = find_last_start_date(target)
    assert actual == expected
