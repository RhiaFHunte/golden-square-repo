from lib.counter import Counter

def test_initial_count_is_zero():
    counter = Counter()
    assert counter.count == 0

def test_add_increases_count():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5
    counter.add(3)
    assert counter.count == 8

def test_report_returns_string():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted 10 so far."