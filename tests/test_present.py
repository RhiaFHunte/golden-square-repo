import pytest 
from lib.present import Present

class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents
    
def test_wrap_and_unwrap():
        present = Present()
        present.wrap("Toy Car")
        assert present.unwrap() == "Toy Car"

def test_wrap_twice_gives_error():
    present = Present()
    present.wrap("Book")
    with pytest.raises(Exception) as error:
        present.wrap("Another Book")
    assert str(error.value) == "A contents has already been wrapped."

def test_unwrap_without_wrap_gives_error():
    present = Present()
    with pytest.raises(Exception) as error:
        present.unwrap()
    assert str(error.value) == "No contents have been wrapped."