from lib.string_builder import StringBuilder

def test_initial_state_is_empty():
    sb = StringBuilder()
    assert sb.output() == ""
    assert sb.size() == 0

def test_add_single_word():
    sb = StringBuilder()
    sb.add("hello")
    assert sb.output() == "hello"
    assert sb.size() == 5

def test_add_multiple_words():
    sb = StringBuilder()
    sb.add("hello")
    sb.add(" world")
    assert sb.output() == "hello world"
    assert sb.size() == 11

def test_add_empty_string_does_not_change():
    sb = StringBuilder()
    sb.add("")
    assert sb.output() == ""
    assert sb.size() == 0
