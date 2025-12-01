from lib.report_length import report_length

def test_short_string():
    result = report_length("hi")
    assert result == "This string was 2 characters long."

def test_long_string():
    result = report_length("Hello world")
    assert result == "This string was 11 characters long."

def test_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."